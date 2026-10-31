import sys, os, math, random; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
WORK = os.environ.get('BURARI_WORK', '/tmp/work')
from lib import *
DUR = 84.384
SHOTS = [(0.0, 6.79, 3.0), (6.79, 18.90, 17.5), (18.90, 23.35, 22.5), (23.35, 30.27, 28.5),
         (30.27, 48.32, 41.0), (48.32, 62.11, 56.0), (62.11, 75.43, 70.0), (75.43, 84.38, 80.0)]
WARM = (1.0, 0.62, 0.3)
def floor(ox, col=(0.05, 0.05, 0.06), size=40): return plane((ox, 0, 0), (size, size), mat(f'fl{ox}', col, 0.5))

def chair(loc, m):
    x, y, z = loc; p = [box((x, y, 0.5), (0.9, 0.9, 0.1), m, bevel=0.02), box((x, y + 0.42, 1.15), (0.9, 0.08, 1.2), m, bevel=0.02)]
    for lx in (-0.4, 0.4):
        for ly in (-0.4, 0.4): p.append(box((x + lx, y + ly, 0.25), (0.07, 0.07, 0.5), m))
    return group(p, loc)

def s1(ox=0):
    t0, t1 = SHOTS[0][:2]
    floor(ox); box((ox, 6, 5), (40, 0.2, 10), mat('bk1', (0.03, 0.03, 0.035), 0.9))
    chair((ox, 0, 0), mat('wood', (0.3, 0.16, 0.08), 0.5))
    am = emat('aura', (1.0, 0.75, 0.4), 6)
    r = torus((ox, 0, 0.03), 1.1, 0.03, am); mkey(am, F(5.3), 6); mkey(am, F(6.4), 0.3)
    yr = text('2007', (ox, 4, 3.4), 2.4, mat('gold', (0.9, 0.6, 0.2), 0.3, metal=1), 0.25); pop(yr, 1.10)
    light_area((ox, -1, 6), 3, 500, WARM); aim(bpy.context.object, (ox, 0, 0))
    L = light_area((ox + 4, 1, 5), 4, 300, (0.6, 0.7, 1.0)); aim(L, (ox, 3, 3))
    camera('C1', t0, t1, (ox + 1.2, -8, 2.4), (ox + 0.3, -5.6, 2.0), (ox, 1, 1.8), (ox, 1, 1.9), 30)

def figure(loc, m, h=1.7):
    x, y, z = loc
    return group([cyl((x, y, z + h*0.37), 0.26, h*0.74, m), sph((x, y, z + h*0.86), 0.2, m)], loc)

def s2(ox=100):
    t0, t1 = SHOTS[1][:2]
    floor(ox)
    figure((ox, 0, 0), mat('lalit', (0.35, 0.37, 0.42), 0.5))
    rm = emat('wave', (0.55, 0.4, 1.0), 6)
    for k in range(4):
        tr = torus((ox, 0, 1.45), 0.3, 0.02, rm, (math.radians(90), 0, 0))
        for c in range(3):
            t = 9.08 + k*0.55 + c*2.2
            key(tr, 'scale', F(t) - 1, (0.001,)*3); key(tr, 'scale', F(t) + 15, (5, 5, 5)); key(tr, 'scale', F(t) + 16, (0.001,)*3)
    om = emat('fam', (1.0, 0.8, 0.5), 2)
    th = emat('thread', (0.55, 0.4, 1.0), 4)
    for i in range(10):
        a = i*2*math.pi/10; x, y = 3.2*math.cos(a), 3.2*math.sin(a)
        sph((ox + x, y, 0.6), 0.22, om)
        c = cyl((ox + x/2, y/2, 1.0), 0.015, 3.2, th, rot=(0, math.radians(90), a)); pop(c, 15.91 + i*0.06)
    mkey(om, F(16.9), 2); mkey(om, F(17.4), 10)
    light_area((ox, -3, 6), 6, 300, (0.8, 0.8, 1.0)); aim(bpy.context.object, (ox, 0, 0))
    c, tg = camera('C2', t0, t1, (ox + 3, -6, 2.2), (ox - 2.5, -7.5, 5.5), (ox, 0, 1.3), (ox, 0, 0.8), 30)

def s3(ox=200):
    t0, t1 = SHOTS[2][:2]
    floor(ox, (0.08, 0.06, 0.05)); box((ox, 3, 3), (14, 0.2, 6), mat('shopwall', (0.2, 0.13, 0.08), 0.8))
    wd = mat('wood', (0.3, 0.16, 0.08), 0.5)
    box((ox - 1.5, 0.5, 0.55), (3.2, 1.0, 1.1), wd, bevel=0.03)
    for z in (1.2, 2.1, 3.0): box((ox - 1.5, 2.6, z), (3.6, 0.7, 0.08), wd)
    rnd = random.Random(2); cols = [(0.6, 0.2, 0.1), (0.2, 0.4, 0.6), (0.8, 0.7, 0.3), (0.3, 0.5, 0.25)]
    for z in (1.2, 2.1, 3.0):
        for k in range(7): box((ox - 3.0 + k*0.45, 2.6, z + 0.25), (0.35, 0.4, 0.42), mat(f'g{k%4}', cols[k % 4], 0.6))
    gold = mat('coin', (1.0, 0.7, 0.2), 0.25, metal=1)
    for i in range(14):
        x = ox - 2.4 + rnd.uniform(0, 1.8); cn = cyl((x, 0.3, 1.15), 0.14, 0.03, gold, rot=(math.radians(90), 0, 0))
        t = 18.9 + i*0.17
        key(cn, 'location', F(t), (x, 0.3, 1.15)); key(cn, 'location', F(t + 2.5), (x + rnd.uniform(-.4, .4), 0.3, 4.5))
        key(cn, 'rotation_euler', F(t), 0.0, 2); key(cn, 'rotation_euler', F(t + 2.5), 6.0, 2)
    bm = emat('bar', (0.3, 1.0, 0.5), 3)
    for k, (h, t) in enumerate(((0.8, 20.02), (1.6, 20.6), (2.6, 21.42))):
        b = box((ox + 0.6 + k*0.7, 0.4, h/2), (0.5, 0.5, h), bm)
        key(b, 'scale', F(t) - 1, (0.5, 0.5, 0.001)); key(b, 'location', F(t) - 1, (ox + 0.6 + k*0.7, 0.4, 0))
        key(b, 'scale', F(t) + 6, (0.5, 0.5, h)); key(b, 'location', F(t) + 6, (ox + 0.6 + k*0.7, 0.4, h/2))
    light_area((ox, -3, 5), 5, 600, WARM); aim(bpy.context.object, (ox, 1, 1))
    camera('C3', t0, t1, (ox - 0.2, -8.5, 2.6), (ox - 0.5, -7.0, 2.4), (ox - 0.5, 1, 2.0), (ox - 0.5, 1, 2.1), 30)

def s4(ox=300):
    t0, t1 = SHOTS[3][:2]
    floor(ox, (0.03, 0.04, 0.03), 60)
    sky((ox, 20, 10), (80, 40), (0.02, 0.03, 0.06), (0.002, 0.003, 0.01), 1.0)
    sph((ox + 4, 18, 13), 1.6, emat('moon', (0.8, 0.85, 1.0), 6))
    bark = mat('bark', (0.12, 0.08, 0.05), 0.9); leaf = mat('leaf', (0.04, 0.12, 0.05), 0.8)
    cyl((ox, 2, 2.5), 0.8, 5, bark, verts=12)
    rnd = random.Random(9)
    for k in range(5): cyl((ox + rnd.uniform(-1, 1), 2, 4.5), 0.25, 5, bark, rot=(0, math.radians(rnd.choice([-55, -40, 40, 55])), 0))
    for k in range(22):
        o = sph((ox + rnd.uniform(-6, 6), 2 + rnd.uniform(-2.5, 2.5), 6.2 + rnd.uniform(-0.3, 1.8)), rnd.uniform(1.2, 2.0), leaf, 1)
    rm = mat('roots', (0.2, 0.14, 0.09), 0.9)
    for k in range(26):
        x = ox + rnd.uniform(-5.5, 5.5); y = 2 + rnd.uniform(-2, 1); L = rnd.uniform(2.5, 5.2)
        r = cyl((x, y, 5.6), 0.05, 1, rm, verts=6)
        t = 26.98 + rnd.uniform(0, 1.6)
        key(r, 'scale', F(t) - 1, (1, 1, 0.001)); key(r, 'location', F(t) - 1, (x, y, 5.6))
        key(r, 'scale', F(t + 1.5), (1, 1, L)); key(r, 'location', F(t + 1.5), (x, y, 5.6 - L/2))
    light_area((ox + 6, -8, 12), 8, 1500, (0.6, 0.7, 1.0)); aim(bpy.context.object, (ox, 2, 3))
    light_point((ox, -2, 1), 60, WARM, 0.3)
    camera('C4', t0, t1, (ox + 2, -21, 2.0), (ox + 0.5, -16, 2.6), (ox, 2, 5), (ox, 2, 4.6), 30)

def s5(ox=400):
    t0, t1 = SHOTS[4][:2]
    floor(ox, (0.02, 0.02, 0.03))
    nm = emat('node', (0.4, 0.8, 1.0), 6); cm = emat('core', (1.0, 0.5, 0.2), 10)
    lm = emat('link', (0.4, 0.8, 1.0), 2)
    for t, c in ((33.5, (0.4, 0.8, 1.0)), (34.1, (1.0, 0.12, 0.08))): mcol(lm, F(t), c); mcol(nm, F(t), c)
    core = sph((ox, 0, 2.5), 0.4, cm)
    rnd = random.Random(4)
    pts = []
    for i in range(11):
        a = i*2*math.pi/11; p = (ox + 2.6*math.cos(a), 2.6*math.sin(a), 2.5 + rnd.uniform(-0.9, 0.9)); pts.append(p)
        sph(p, 0.18, nm)
    from mathutils import Vector
    def link(p, q):
        p, q = Vector(p), Vector(q); d = q - p; mid = (p + q)/2
        o = cyl(mid, 0.018, d.length, lm, verts=8); o.rotation_euler = d.to_track_quat('Z', 'Y').to_euler(); return o
    for p in pts: link((ox, 0, 2.5), p)
    for i in range(11): link(pts[i], pts[(i + 1) % 11])
    gm = emat('outsider', (0.6, 0.6, 0.6), 3); g = sph((ox + 4.6, -1.2, 3.6), 0.3, gm)
    mkey(gm, F(46.0), 3); mkey(gm, F(47.4), 0); key(g, 'scale', F(46.0), (1, 1, 1)); key(g, 'scale', F(47.4), (0.001,)*3)
    camera('C5', t0, t1, (ox - 6, -9, 10), (ox + 6, -8, 8.5), (ox, 0, 2.2), (ox, 0, 2.3), 30)

def s6(ox=500):
    t0, t1 = SHOTS[5][:2]
    floor(ox, (0.02, 0.02, 0.03))
    rnd = random.Random(6); wm = emat('qwhite', (0.85, 0.9, 1.0), 2.5)
    for k in range(9):
        q = text('?', (ox + rnd.uniform(-3.5, 3.5), rnd.uniform(1, 6), rnd.uniform(1.5, 7)), rnd.uniform(0.6, 1.6), wm, 0.12)
        key(q, 'rotation_euler', F(t0), rnd.uniform(-0.6, 0), 2); key(q, 'rotation_euler', F(t1), rnd.uniform(0, 0.6), 2)
    ring = torus((ox, -2, 3.4), 0.9, 0.11, mat('ringg', (1.0, 0.75, 0.3), 0.2, metal=1), (math.radians(80), 0, 0))
    sph((ox, -2, 4.35), 0.18, mat('gem', (0.9, 0.95, 1.0), 0.0, emit=(0.8, 0.9, 1.0), strength=4))
    pop(ring, 53.5); key(ring, 'rotation_euler', F(53.5), 0, 2); key(ring, 'rotation_euler', F(62), 3.0, 2)
    rq = text('?', (ox, 2, 4.0), 3.6, emat('qred2', (1.0, 0.08, 0.05), 6), 0.35); pop(rq, 61.22)
    light_area((ox, -4, 6), 5, 400, (1, 0.9, 0.8)); aim(bpy.context.object, (ox, 0, 3))
    camera('C6', t0, t1, (ox, -12, 3.6), (ox, -8.5, 3.9), (ox, 0, 3.8), (ox, 0, 3.8), 32)

def s7(ox=600):
    t0, t1 = SHOTS[6][:2]
    house(ox, lit=False, door_open=False)
    sky((ox, 25, 12), (90, 40), (0.004, 0.006, 0.015), (0.01, 0.012, 0.03), 1.0)
    box((ox + 2.2, -4.02, 7.7), (1.6, 0.05, 1.5), emat('onewin', (1.0, 0.62, 0.3), 4))
    light_area((ox, -12, 20), 30, 300, (0.5, 0.6, 1.0), (math.radians(30), 0, 0))
    rain = emat('rain', (0.6, 0.7, 0.9), 1.5); rnd = random.Random(11)
    for k in range(160):
        x = ox + rnd.uniform(-8, 8); y = rnd.uniform(-20, -6); dur = rnd.uniform(0.7, 1.1); ph = rnd.uniform(0, dur)
        d = cyl((x, y, 14), 0.008, 0.5, rain, verts=4)
        key(d, 'location', 0, (x, y, 14)); key(d, 'location', F(dur), (x, y, 0))
        for fc in d.animation_data.action.fcurves if hasattr(d.animation_data.action, 'fcurves') else d.animation_data.action.layers[0].strips[0].channelbags[0].fcurves:
            for kp in fc.keyframe_points: kp.interpolation = 'LINEAR'
            fc.modifiers.new('CYCLES')
        d.location.z = 14
    camera('C7', t0, t1, (ox - 1, -30, 5), (ox + 0.5, -20, 6.5), (ox, 0, 5.5), (ox + 1, 0, 6.5), 32)

def s8(ox=700):
    t0, t1 = SHOTS[7][:2]
    floor(ox, (0.02, 0.02, 0.03))
    a = text('SHARED\nPSYCHOSIS?', (ox, 0, 4.85), 0.8, mat('cy', (0.3, 0.85, 1.0), 0.4, emit=(0.3, 0.85, 1.0), strength=0.6), 0.15); pop(a, 77.26)
    o = text('OR', (ox, 0, 3.65), 0.5, mat('orw', (0.8, 0.8, 0.8), 0.4), 0.08); pop(o, 78.80)
    b = text('SOMETHING\nELSE?', (ox, 0, 2.45), 0.8, mat('or8', (1.0, 0.54, 0.0), 0.4, emit=(1.0, 0.54, 0.0), strength=0.6), 0.15); pop(b, 78.99)
    light_area((ox, -5, 4), 5, 700); aim(bpy.context.object, (ox, 0, 3))
    camera('C8', t0, t1, (ox - 1, -9, 2.4), (ox + 0.8, -7.4, 3.2), (ox, 0, 3.3), (ox, 0, 3.3), 32)

def build():
    s = setup(DUR)
    for f in (s1, s2, s3, s4, s5, s6, s7, s8): f()
    return s
if __name__ == '__main__':
    run(build, SHOTS, WORK + '/p2')
