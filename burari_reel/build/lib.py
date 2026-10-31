import bpy, math, random
from mathutils import Vector
FPS = 15
def F(t): return int(round(t * FPS))
FONT = None
def setup(dur, res_pct=50, samples=8):
    global FONT
    bpy.ops.wm.read_factory_settings(use_empty=True)
    s = bpy.context.scene
    s.render.engine = 'CYCLES'; s.cycles.device = 'CPU'
    s.cycles.samples = samples; s.cycles.adaptive_min_samples = 4; s.cycles.use_denoising = True; s.cycles.denoiser = 'OPENIMAGEDENOISE'
    s.cycles.max_bounces = 4; s.cycles.diffuse_bounces = 2; s.cycles.glossy_bounces = 2
    s.cycles.transmission_bounces = 2; s.cycles.transparent_max_bounces = 8
    s.cycles.caustics_reflective = False; s.cycles.caustics_refractive = False
    s.cycles.use_adaptive_sampling = True; s.cycles.adaptive_threshold = 0.05
    s.render.use_persistent_data = True
    s.render.resolution_x = 1080; s.render.resolution_y = 1920; s.render.resolution_percentage = res_pct
    s.render.fps = FPS; s.frame_start = 0; s.frame_end = int(math.ceil(dur * FPS)) - 1
    s.render.image_settings.file_format = 'PNG'
    s.view_settings.view_transform = 'AgX'; s.view_settings.look = 'AgX - Medium High Contrast'
    w = bpy.data.worlds.new('W'); s.world = w; w.use_nodes = True
    bg = w.node_tree.nodes['Background']; bg.inputs[0].default_value = (0.006, 0.007, 0.012, 1); bg.inputs[1].default_value = 1
    import os; FONT = bpy.data.fonts.load(os.environ.get('BURARI_FONT', '/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf'))
    # compositor bloom
    s.render.compositor_device = 'CPU'
    ng = bpy.data.node_groups.new('Comp', 'CompositorNodeTree'); s.compositing_node_group = ng
    rl = ng.nodes.new('CompositorNodeRLayers'); gl = ng.nodes.new('CompositorNodeGlare')
    gl.inputs['Type'].default_value = 'Bloom'
    try: gl.inputs['Quality'].default_value = 'Medium'
    except Exception: pass
    gl.inputs['Threshold'].default_value = 0.9; gl.inputs['Strength'].default_value = 0.6; gl.inputs['Size'].default_value = 0.6
    out = ng.interface.new_socket('Image', in_out='OUTPUT', socket_type='NodeSocketColor')
    go = ng.nodes.new('NodeGroupOutput')
    ng.links.new(rl.outputs['Image'], gl.inputs['Image']); ng.links.new(gl.outputs['Image'], go.inputs[0])
    return s

_mats = {}
def mat(name, color=(0.5,0.5,0.5), rough=0.6, emit=None, strength=0.0, metal=0.0, alpha=1.0):
    key = (name,)
    if key in _mats: return _mats[key]
    m = bpy.data.materials.new(name); m.use_nodes = True
    p = m.node_tree.nodes['Principled BSDF']
    p.inputs['Base Color'].default_value = (*color, 1); p.inputs['Roughness'].default_value = rough
    p.inputs['Metallic'].default_value = metal
    if emit is not None:
        p.inputs['Emission Color'].default_value = (*emit, 1); p.inputs['Emission Strength'].default_value = strength
    if alpha < 1: p.inputs['Alpha'].default_value = alpha
    _mats[key] = m; return m
def emat(name, color, strength): return mat(name, (0,0,0), 1.0, color, strength)

def _fin(o, m, name=None):
    if m: o.data.materials.append(m)
    if name: o.name = name
    return o
def box(loc, size, m=None, rot=(0,0,0), bevel=0.0):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc, rotation=rot); o = bpy.context.object
    o.scale = size
    if bevel:
        md = o.modifiers.new('b', 'BEVEL'); md.width = bevel; md.segments = 2
    return _fin(o, m)
def cyl(loc, r, h, m=None, rot=(0,0,0), verts=24):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=h, location=loc, rotation=rot); return _fin(bpy.context.object, m)
def sph(loc, r, m=None, sub=3):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=sub, radius=r, location=loc); o = bpy.context.object
    bpy.ops.object.shade_smooth(); return _fin(o, m)
def torus(loc, R, r, m=None, rot=(0,0,0)):
    bpy.ops.mesh.primitive_torus_add(major_radius=R, minor_radius=r, location=loc, rotation=rot, major_segments=48, minor_segments=12)
    o = bpy.context.object; bpy.ops.object.shade_smooth(); return _fin(o, m)
def plane(loc, size, m=None, rot=(0,0,0)):
    bpy.ops.mesh.primitive_plane_add(size=1, location=loc, rotation=rot); o = bpy.context.object; o.scale = (size[0], size[1], 1); return _fin(o, m)
def text(body, loc, size, m, extrude=0.08, rot=(math.pi/2,0,0), align='CENTER'):
    c = bpy.data.curves.new('T', 'FONT'); c.body = body; c.font = FONT; c.size = size
    c.align_x = align; c.align_y = 'CENTER'; c.extrude = extrude; c.bevel_depth = extrude*0.15; c.bevel_resolution = 1
    o = bpy.data.objects.new('T', c); bpy.context.collection.objects.link(o)
    o.location = loc; o.rotation_euler = rot; c.materials.append(m); return o
def light_area(loc, size, power, color=(1,1,1), rot=(0,0,0)):
    d = bpy.data.lights.new('A', 'AREA'); d.size = size; d.energy = power; d.color = color
    o = bpy.data.objects.new('A', d); bpy.context.collection.objects.link(o); o.location = loc; o.rotation_euler = rot; return o
def light_point(loc, power, color=(1,1,1), r=0.1):
    d = bpy.data.lights.new('P', 'POINT'); d.energy = power; d.color = color; d.shadow_soft_size = r
    o = bpy.data.objects.new('P', d); bpy.context.collection.objects.link(o); o.location = loc; return o
def aim(o, target):
    d = Vector(target) - o.location; o.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()

def key(o, path, f, val, idx=-1):
    if isinstance(val, (tuple, list)): setattr(o, path, val)
    else:
        if idx >= 0: getattr(o, path)[idx] = val
        else: setattr(o, path, val)
    o.keyframe_insert(path, frame=f, index=idx)
def pop(o, t, scale=None, dur=6):
    """scale/opacity pop with overshoot, starting at the spoken word"""
    s = tuple(scale or o.scale); f = F(t)
    key(o, 'scale', f - 1, (0.0001,)*3); key(o, 'scale', f + dur//2, tuple(v*1.18 for v in s)); key(o, 'scale', f + dur, s)
def move(o, t0, t1, a, b):
    key(o, 'location', F(t0), a); key(o, 'location', F(t1), b)
def mkey(m, f, strength):
    p = m.node_tree.nodes['Principled BSDF'].inputs['Emission Strength']; p.default_value = strength; p.keyframe_insert('default_value', frame=f)
def mcol(m, f, col):
    p = m.node_tree.nodes['Principled BSDF'].inputs['Emission Color']; p.default_value = (*col, 1); p.keyframe_insert('default_value', frame=f)

def camera(name, t0, t1, a, b, ta, tb, lens=35):
    d = bpy.data.cameras.new(name); d.lens = lens; d.clip_end = 400
    c = bpy.data.objects.new(name, d); bpy.context.collection.objects.link(c)
    tgt = bpy.data.objects.new(name + '_t', None); bpy.context.collection.objects.link(tgt)
    con = c.constraints.new('TRACK_TO'); con.target = tgt; con.track_axis = 'TRACK_NEGATIVE_Z'; con.up_axis = 'UP_Y'
    move(c, t0, t1, a, b); move(tgt, t0, t1, ta, tb)
    s = bpy.context.scene; mk = s.timeline_markers.new(name, frame=F(t0)); mk.camera = c
    if s.camera is None: s.camera = c
    return c, tgt
def campath(c, pts):
    """extra camera keys: list of (t, loc)"""
    for t, l in pts: key(c, 'location', F(t), l)

# ---------- reusable models ----------
def house(ox, oy=0, night=True, door_open=True, lit=True, shutter=True):
    conc = mat('conc', (0.36, 0.32, 0.28), 0.85)
    dark = mat('dark', (0.05, 0.05, 0.06), 0.7)
    nb = mat('neighbour', (0.12, 0.12, 0.14), 0.9)
    win_on = emat('win_on', (1.0, 0.62, 0.3), 3.0)
    win_off = mat('win_off', (0.02, 0.025, 0.04), 0.2)
    shut = mat('shutter', (0.25, 0.27, 0.3), 0.4, metal=0.6)
    W, D, H = 8, 8, 9
    box((ox, oy, H/2), (W, D, H), conc)
    box((ox, oy, H + 0.4), (W + 0.2, D + 0.2, 0.2), conc)          # roof slab
    for x in (-W/2, W/2): box((ox + x, oy, H + 0.9), (0.15, D, 0.8), conc)  # parapet sides
    box((ox, oy - D/2, H + 0.9), (W, 0.15, 0.8), conc)
    box((ox, oy - D/2 - 0.6, 3.2), (W + 0.4, 1.2, 0.18), conc)      # balcony
    box((ox, oy - D/2 - 1.15, 3.7), (W + 0.4, 0.06, 0.9), mat('rail', (0.05,0.05,0.05), 0.4, metal=0.8))
    for fl in (1, 2):
        for wx in (-2.2, 2.2):
            on = lit and not (fl == 2 and wx > 0)
            box((ox + wx, oy - D/2 - 0.01, 1.9 + fl*2.9), (1.6, 0.05, 1.5), win_on if on else win_off)
            box((ox + wx, oy - D/2 - 0.08, 1.9 + fl*2.9 - 0.8), (1.9, 0.18, 0.1), conc)
    # ground floor: two shutters + door
    for sx in (-2.6, 2.6):
        if shutter:
            box((ox + sx, oy - D/2 - 0.05, 1.3), (2.4, 0.1, 2.6), shut)
            for k in range(12): box((ox + sx, oy - D/2 - 0.11, 0.15 + k*0.22), (2.4, 0.04, 0.05), dark)
    box((ox, oy - D/2 - 0.02, 1.25), (1.4, 0.06, 2.5), emat(f'doorlight{ox}', (1.0, 0.7, 0.38), 6.0 if door_open else 0.0)); house.doorlight = _mats[(f'doorlight{ox}',)]
    door = hinge_door((ox - 0.7, oy - D/2 - 0.1, 1.25), 1.4, 2.45, mat('door', (0.25, 0.14, 0.08), 0.5), 55 if door_open else 0)
    # neighbours + street
    rnd = random.Random(int(ox) + 7)
    for side in (-1, 1):
        for k in range(3):
            h = rnd.uniform(6, 12); x = ox + side*(W/2 + 4.2 + k*8.4)
            box((x, oy + rnd.uniform(-0.5, 1), h/2), (8.2, 8, h), nb)
            for j in range(int(h // 3)):
                if rnd.random() < 0.35: box((x + rnd.uniform(-2, 2), oy - 4.05, 2 + j*3), (1.4, 0.05, 1.2), win_on if night else win_off)
    plane((ox, oy - 10, 0), (80, 30), mat('road', (0.05, 0.05, 0.055), 0.6))
    box((ox, oy - 5.2, 0.08), (60, 2, 0.16), mat('kerb', (0.18, 0.18, 0.19), 0.8))
    for x in (-7, 9):
        cyl((ox + x, oy - 6, 3), 0.08, 6, dark)
        sph((ox + x, oy - 6.6, 5.9), 0.25, emat('lamp', (1.0, 0.75, 0.45), 25.0))
        light_point((ox + x, oy - 6.6, 5.6), 400 if night else 80, (1.0, 0.75, 0.45), 0.3)
    return door

def dog(loc, m, rotz=0):
    parts = []
    x, y, z = loc
    parts.append(box((x, y, z + 0.55), (0.9, 0.35, 0.35), m, bevel=0.08))
    parts.append(box((x + 0.55, y, z + 0.85), (0.38, 0.3, 0.32), m, bevel=0.08))
    parts.append(box((x + 0.78, y, z + 0.8), (0.18, 0.18, 0.14), m, bevel=0.04))
    for ex in (-0.09, 0.09): parts.append(box((x + 0.5, y + ex, z + 1.05), (0.08, 0.06, 0.16), m))
    for lx in (-0.35, 0.35):
        for ly in (-0.12, 0.12): parts.append(box((x + lx, y + ly, z + 0.2), (0.1, 0.1, 0.4), m))
    parts.append(box((x - 0.55, y, z + 0.75), (0.35, 0.07, 0.07), m, rot=(0, math.radians(-40), 0)))
    emp = group(parts, loc); emp.rotation_euler.z = rotz
    return emp
def group(objs, loc):
    emp = bpy.data.objects.new('grp', None); bpy.context.collection.objects.link(emp); emp.location = loc
    bpy.context.view_layer.update()
    for p in objs:
        p.parent = emp; p.matrix_parent_inverse = emp.matrix_world.inverted()
    return emp
def diary(loc, color, rot=(0,0,0), size=(0.9, 1.25, 0.14)):
    b = box(loc, size, mat('cov%.2f%.2f' % color[:2], color, 0.55), rot=rot, bevel=0.02)
    p = box((loc[0] + 0.02, loc[1], loc[2]), (size[0]*0.96, size[1]*0.94, size[2]*0.8), mat('paper', (0.85, 0.8, 0.68), 0.9), rot=rot)
    return group([b, p], loc)

def sky(loc, size, low, high, strength=1.0, rot=(math.pi/2, 0, 0)):
    m = bpy.data.materials.new('sky'); m.use_nodes = True; nt = m.node_tree
    for n in list(nt.nodes): nt.nodes.remove(n)
    tc = nt.nodes.new('ShaderNodeTexCoord'); sx = nt.nodes.new('ShaderNodeSeparateXYZ')
    cr = nt.nodes.new('ShaderNodeValToRGB'); em = nt.nodes.new('ShaderNodeEmission'); out = nt.nodes.new('ShaderNodeOutputMaterial')
    cr.color_ramp.elements[0].color = (*low, 1); cr.color_ramp.elements[1].color = (*high, 1)
    nt.links.new(tc.outputs['Generated'], sx.inputs[0]); nt.links.new(sx.outputs['Y'], cr.inputs[0])
    nt.links.new(cr.outputs[0], em.inputs[0]); em.inputs[1].default_value = strength; nt.links.new(em.outputs[0], out.inputs[0])
    return plane(loc, size, m, rot)

def hinge_door(hloc, w, h, m, open_deg=0):
    d = box((hloc[0] + w/2, hloc[1], hloc[2]), (w, 0.08, h), m)
    hg = group([d], hloc); hg.rotation_euler.z = math.radians(-open_deg); return hg

def run(build, shots, outdir):
    import sys, os
    argv = sys.argv[sys.argv.index('--'):] if '--' in sys.argv else sys.argv  # blender -b --python x.py -- args
    mode = argv[1] if len(argv) > 1 else 'stills'
    s = build()
    os.makedirs(outdir, exist_ok=True)
    if mode == 'save':
        bpy.ops.wm.save_as_mainfile(filepath=outdir + '/scene.blend'); return
    if mode == 'stills':
        bpy.ops.wm.save_as_mainfile(filepath=outdir + '/scene.blend')
        which = [int(x) for x in argv[2].split(',')] if len(argv) > 2 else range(len(shots))
        for i in which:
            t = shots[i][2] if len(shots[i]) > 2 else (shots[i][0] + shots[i][1]) / 2
            s.frame_set(F(t)); s.render.filepath = f'{outdir}/still_{i+1:02d}.png'
            bpy.ops.render.render(write_still=True); print('STILL', i+1, F(t), flush=True)
    if mode == 'anim':
        s.frame_start = int(argv[2]); s.frame_end = min(int(argv[3]), s.frame_end)
        s.render.filepath = outdir + '/frames/'; s.render.use_overwrite = False; s.render.use_placeholder = True
        bpy.ops.render.render(animation=True)
