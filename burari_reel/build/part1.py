import sys, os, math, random; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
WORK = os.environ.get('BURARI_WORK', '/tmp/work')
from lib import *
DUR = 116.28
SHOTS = [(0.00, 6.04, 2.2), (6.04, 24.38, 19.0), (24.38, 40.37, 32.5), (40.37, 55.85, 51.0),
         (55.85, 61.01, 59.0), (61.01, 83.49, 75.0), (83.49, 106.08, 97.0), (106.08, 116.28, 112.5)]
WARM = (1.0, 0.62, 0.3)

def s1(ox=0):
    t0, t1 = SHOTS[0][:2]
    house(ox)
    light_area((ox, -12, 20), 30, 600, (0.5, 0.6, 1.0), (math.radians(30), 0, 0))
    light_area((ox, -4.3, 1.3), 1.2, 180, WARM, (math.radians(-90), 0, 0))   # door spill
    plane((ox, -5.6, 0.17), (1.6, 2.4), emat('spill', WARM, 1.2))
    sky((ox, 25, 12), (90, 40), (0.004, 0.006, 0.015), (0.01, 0.012, 0.03), 1.0)
    om = emat('orb', (1.0, 0.85, 0.6), 12)
    for i in range(11):
        a = math.radians(-60 + i * 12); o = sph((ox + 7.2*math.sin(a), 0, 12.5 + 2.2*math.cos(a)), 0.32, om)
        pop(o, t0 + 0.04*i)
    camera('C1', t0, t1, (ox, -36, 3.5), (ox, -24, 4.8), (ox, 0, 7), (ox, 0, 6.8), 35)

def s2(ox=100):
    t0, t1 = SHOTS[1][:2]
    door = house(ox, night=False, door_open=False, lit=False)
    sky((ox, 25, 14), (110, 50), (0.9, 0.42, 0.2), (0.12, 0.18, 0.35), 1.6)
    light_area((ox - 20, -25, 12), 40, 4000, (1.0, 0.7, 0.5), (0, 0, 0)); aim(bpy.context.object, (ox, 0, 3))
    light_area((ox + 10, -20, 25), 30, 1500, (0.6, 0.7, 1.0)); aim(bpy.context.object, (ox, 0, 0))
    # neighbour walking marker + path dots
    nm = emat('walker', (0.5, 0.85, 1.0), 3)
    w = group([cyl((ox - 22, -6.3, 0.75), 0.16, 1.1, nm), sph((ox - 22, -6.3, 1.5), 0.17, nm)], (ox - 22, -6.3, 0))
    move(w, 10.84, 17.0, (ox - 22, -6.3, 0), (ox - 1.2, -6.0, 0))
    for k in range(14):
        d = cyl((ox - 21 + k*1.5, -6.3, 0.18), 0.12, 0.03, nm); pop(d, 10.84 + k*0.42)
    # shop shut: shutters glow red outline at "बंद"
    rm = emat('shutred', (1.0, 0.1, 0.05), 0.0); mkey(rm, F(20.6), 0); mkey(rm, F(21.0), 6); mkey(rm, F(23.0), 3)
    for sx in (-2.6, 2.6):
        for zz in (0.02, 2.62): box((ox + sx, -4.17, zz), (2.5, 0.04, 0.05), rm)
        for xx in (-1.24, 1.24): box((ox + sx + xx, -4.17, 1.32), (0.05, 0.04, 2.6), rm)
    # door swings open at "खुला"
    key(door, 'rotation_euler', F(22.9), 0.0, 2); key(door, 'rotation_euler', F(23.6), math.radians(-50), 2)
    dl = house.doorlight; mkey(dl, F(22.9), 0); mkey(dl, F(23.6), 5)
    c, tg = camera('C2', t0, t1, (ox - 14, -34, 3.0), (ox - 0.6, -13.5, 1.9), (ox - 2, 0, 3), (ox, -4, 1.6), 35)
    campath(c, [(17.0, (ox - 6, -22, 2.4))]); campath(tg, [(17.0, (ox - 1, -2, 2.0))])

def s3(ox=200):
    t0, t1 = SHOTS[2][:2]
    wall = mat('plaster3', (0.09, 0.085, 0.08), 0.9)
    # stairs up along +y
    for k in range(12): box((ox, 0.3 + k*0.5, 0.15 + k*0.3), (2.4, 0.5, 0.3 + k*0.6 if False else 0.3), wall)
    for k in range(12): box((ox, 0.3 + k*0.5, (k*0.3)/2), (2.4, 0.5, k*0.3 + 0.01), wall)
    for x in (-1.3, 1.3): box((ox + x, 3, 3), (0.1, 8, 7), wall)
    box((ox, 10, 3.55), (12, 8, 0.1), mat('floor', (0.3, 0.27, 0.24), 0.7))  # upper floor
    box((ox, 14, 5.3), (12, 0.2, 3.6), wall)
    for x in (-6, 6): box((ox + x, 10, 5.3), (0.2, 8, 3.6), wall)
    # ceiling with opening + iron grille (jaali)
    cz = 7.1; ceil = mat('ceil', (0.18, 0.17, 0.16), 0.9)
    box((ox - 4.5, 10, cz), (3, 8, 0.2), ceil); box((ox + 4.5, 10, cz), (3, 8, 0.2), ceil)
    box((ox, 6.9, cz), (6, 1.8, 0.2), ceil); box((ox, 13.1, cz), (6, 1.8, 0.2), ceil)
    iron = mat('iron', (0.04, 0.04, 0.045), 0.35, metal=0.9)
    for i in range(13): box((ox - 3 + i*0.5, 10, cz), (0.05, 4.4, 0.05), iron)
    for j in range(10): box((ox, 7.8 + j*0.48, cz), (6, 0.05, 0.05), iron)
    light_area((ox, 10, cz + 3), 5, 2500, (0.75, 0.82, 1.0))    # cold daylight through grille
    light_point((ox, 1, 2.5), 60, WARM, 0.3)
    om = emat('hang', (1.0, 0.75, 0.45), 6)
    rnd = random.Random(3); pts = [(ox - 2.5 + (i % 5)*1.25 + rnd.uniform(-.2,.2), 8.8 + (i // 5)*2.2) for i in range(10)]
    for i, (x, y) in enumerate(pts):
        wv = cyl((x, y, cz - 0.7), 0.008, 1.4, iron); o = sph((x, y, cz - 1.45), 0.13, om)
        pop(wv, 31.06 + 0.06*i); pop(o, 31.06 + 0.06*i)
    for t, v in ((32.0, 6), (33.3, 4.5), (35.1, 3.2), (36.8, 2.2), (38.6, 1.4)): mkey(om, F(t), v)
    c, tg = camera('C3', t0, t1, (ox, -3.5, 1.6), (ox, 6.4, 4.9), (ox, 6, 3.8), (ox, 10.2, 6.6), 28)
    campath(c, [(29.5, (ox, 3.5, 3.6))]); campath(tg, [(29.5, (ox, 9, 5.8))])

def s4(ox=300):
    t0, t1 = SHOTS[3][:2]
    wall = mat('plaster', (0.22, 0.2, 0.19), 0.9)
    box((ox, 0, -0.05), (8, 8, 0.1), mat('floor', (0.3, 0.27, 0.24), 0.7))
    box((ox, 4, 2), (8, 0.2, 4), wall); box((ox - 4, 0, 2), (0.2, 8, 4), wall)
    box((ox + 1.5, 3.9, 2.2), (1.6, 0.05, 1.4), emat('moonwin', (0.5, 0.6, 1.0), 2.5))
    box((ox - 2.3, 2.4, 0.3), (2.2, 1.2, 0.6), mat('bed', (0.3, 0.12, 0.1), 0.8))      # charpai/bed
    gm = emat('grandma', (1.0, 0.8, 0.55), 8); g = sph((ox - 0.6, 0.6, 0.18), 0.18, gm); pop(g, 41.31)
    mkey(gm, F(43.0), 8); mkey(gm, F(45.5), 3)
    light_area((ox + 1.5, 2.5, 2.4), 2, 120, (0.55, 0.65, 1.0), (math.radians(80), 0, math.radians(180)))
    light_point((ox - 0.6, 0.6, 1.2), 25, WARM)
    # terrace to the right
    tx = ox + 14
    box((tx, 0, -0.05), (10, 10, 0.1), mat('terr', (0.25, 0.24, 0.23), 0.85))
    box((tx, 5, 0.5), (10, 0.2, 1), wall); box((tx + 5, 0, 0.5), (0.2, 10, 1), wall)
    cyl((tx + 3, 3, 1), 1, 2, mat('tank', (0.05, 0.05, 0.05), 0.4))
    sky((tx, 15, 6), (60, 25), (0.02, 0.03, 0.07), (0.003, 0.004, 0.012), 1.0)
    pipe = cyl((tx - 1.8, 1.5, 0.9), 0.06, 1.8, mat('pipe', (0.3, 0.3, 0.32), 0.3, metal=1))
    dm = mat('dogfur', (0.55, 0.38, 0.22), 0.8)
    dg = dog((tx - 0.2, 0.2, 0), dm, math.radians(200)); pop(dg, 48.83)
    ch = mat('chain', (0.5, 0.5, 0.52), 0.25, metal=1)
    for k in range(8):
        torus((tx - 1.8 + k*0.2, 1.5 - k*0.16, 0.5 - k*0.03), 0.06, 0.012, ch, (0, math.radians(90*(k%2)), math.radians(-40)))
    light_area((tx - 3, -4, 5), 4, 500, (0.55, 0.65, 1.0)); aim(bpy.context.object, (tx, 0, 0))
    light_point((tx - 0.2, -1.2, 1.5), 40, WARM)
    c, tg = camera('C4', t0, t1, (ox + 1.5, -5.5, 2.4), (tx + 0.6, -3.6, 1.4), (ox - 1, 1.2, 0.4), (tx - 0.6, 0.6, 0.6), 30)
    campath(c, [(46.1, (ox + 0.6, -4.2, 1.6)), (48.8, (tx + 1.5, -6, 2.2))]); campath(tg, [(46.1, (ox - 0.6, 0.8, 0.3)), (48.8, (tx - 0.4, 0.5, 0.6))])

def s5(ox=400):
    t0, t1 = SHOTS[4][:2]
    yel = mat('tape', (0.95, 0.75, 0.02), 0.5); blk = mat('tapetxt', (0.02, 0.02, 0.02), 0.6)
    for ang, z in ((12, 3.3), (-9, 2.0)):
        r = math.radians(ang); bx = box((ox, -2, z), (16, 0.02, 0.55), yel, rot=(0, -r, 0))
        for k in range(-3, 4):
            x = k*2.4; tt = text('POLICE LINE', (ox + x*math.cos(r), -2.03, z + x*math.sin(r)), 0.3, blk, 0.005, (math.pi/2, -r, 0) if False else (math.pi/2, 0, 0))
            tt.rotation_euler = (math.pi/2, r, 0) if False else (math.pi/2, 0, 0); tt.rotation_mode = 'XYZ'; tt.rotation_euler = (math.radians(90), math.radians(-ang), 0) if False else (math.radians(90), 0, 0)
            tt.rotation_euler.y = -r
    q = text('?', (ox, 3, 6.2), 4.5, emat('qred', (1.0, 0.08, 0.05), 6), 0.4)
    pop(q, 57.36); key(q, 'rotation_euler', F(55.9), math.radians(-25), 2); key(q, 'rotation_euler', F(61.0), math.radians(25), 2)
    box((ox, 6, 3), (30, 0.2, 12), mat('back', (0.02, 0.02, 0.03), 0.9))
    r1 = light_point((ox - 6, 1, 4), 0, (1, 0.05, 0.05), 1); b1 = light_point((ox + 6, 1, 4), 0, (0.1, 0.25, 1), 1)
    for k in range(0, 16):
        f = F(t0) + k*5
        key(r1.data, 'energy', f, 2500 if k % 2 == 0 else 50); key(b1.data, 'energy', f, 50 if k % 2 == 0 else 2500)
    light_area((ox, -6, 6), 6, 150, (1, 1, 1)); aim(bpy.context.object, (ox, 0, 2.5))
    camera('C5', t0, t1, (ox - 1.5, -13, 2.2), (ox + 0.8, -10, 2.4), (ox, 2, 4.6), (ox, 2, 4.8), 35)

def stool(loc, m):
    parts = [cyl((loc[0], loc[1], loc[2] + 0.45), 0.22, 0.05, m)]
    for k in range(3):
        a = k*2.094; parts.append(cyl((loc[0] + 0.15*math.cos(a), loc[1] + 0.15*math.sin(a), loc[2] + 0.22), 0.025, 0.45, m))
    return group(parts, loc)
def s6(ox=500):
    t0, t1 = SHOTS[5][:2]
    door = house(ox)
    sky((ox, 25, 12), (90, 40), (0.004, 0.006, 0.015), (0.01, 0.012, 0.03), 1.0)
    light_area((ox, -12, 20), 30, 500, (0.5, 0.6, 1.0), (math.radians(30), 0, 0))
    light_area((ox, -4.3, 1.3), 1.2, 150, WARM, (math.radians(-90), 0, 0))
    # CCTV camera in foreground
    cm = mat('cctv', (0.85, 0.85, 0.85), 0.4)
    cc = [box((ox - 3.2, -17.5, 6.6), (0.5, 1.2, 0.45), cm, rot=(math.radians(-12), 0, 0), bevel=0.05),
          cyl((ox - 3.2, -16.9, 6.5), 0.16, 0.1, emat('rec', (1, 0.05, 0.05), 8), rot=(math.radians(78), 0, 0))]
    # holographic clock
    cyan = emat('holo', (0.2, 0.85, 1.0), 6)
    clk = (ox + 2.2, -8, 10.6)
    torus(clk, 1.3, 0.05, cyan, (math.radians(90), 0, 0))
    for k in range(12):
        a = k*math.pi/6; box((clk[0] + 1.1*math.sin(a), clk[1], clk[2] + 1.1*math.cos(a)), (0.05, 0.03, 0.2), cyan, rot=(0, a, 0))
    def hand(L, w):
        h = box((clk[0], clk[1] - 0.05, clk[2] + L/2), (w, 0.03, L), cyan); return group([h], clk)
    hh, mh = hand(0.6, 0.09), hand(0.95, 0.05)
    for t, hrs, mins in ((61.0, 9, 58), (64.03, 10, 0), (67.8, 10, 15), (72.4, 10, 40), (75.69, 10, 57), (83.5, 11, 4)):
        key(mh, 'rotation_euler', F(t), mins/60*2*math.pi, 1); key(hh, 'rotation_euler', F(t), (hrs % 12 + mins/60)/12*2*math.pi, 1)
    # 5 stools into the house
    sm = mat('stoolm', (0.6, 0.12, 0.08), 0.5)
    for i in range(5):
        st = stool((ox - 12, -6.6, 0.16), sm); t = 65.28 + i*0.3
        key(st, 'location', F(t) - 1, (ox - 14, -6.6, 0.16)); key(st, 'location', F(t + 1.2), (ox - 0.3, -5.6, 0.16))
        key(st, 'scale', F(t + 1.2), (1, 1, 1)); key(st, 'scale', F(t + 1.5), (0.001,)*3)
    # teens with wire coil
    tm = emat('teen', (0.5, 0.85, 1.0), 6); om = emat('wire', (1.0, 0.45, 0.05), 8)
    for j, dx in enumerate((0, 0.8)):
        p = cyl((ox + 14 + dx, -6.6, 0.8), 0.2, 1.3, tm); move(p, 69.38, 71.4, (ox + 14 + dx, -6.6, 0.8), (ox + 0.2 + dx*0.4, -5.6, 0.8))
        key(p, 'scale', F(71.4), (1, 1, 1)); key(p, 'scale', F(71.7), (0.001,)*3)
    coil = torus((ox + 14.4, -6.9, 1.2), 0.35, 0.05, om, (math.radians(90), 0, 0))
    move(coil, 69.38, 71.4, (ox + 14.4, -6.9, 1.2), (ox + 0.6, -5.9, 1.2)); key(coil, 'scale', F(71.4), (1,1,1)); key(coil, 'scale', F(71.7), (0.001,)*3)
    pop(coil, 69.38)
    # food delivery
    fb = box((ox - 14, -6.7, 1.0), (0.5, 0.4, 0.3), mat('foodbox', (0.75, 0.55, 0.3), 0.7)); pop(fb, 74.02)
    move(fb, 74.02, 75.2, (ox - 14, -6.7, 1.0), (ox - 0.2, -5.7, 1.0)); key(fb, 'scale', F(75.2), (1,1,1)); key(fb, 'scale', F(75.5), (0.001,)*3)
    # dog walk out and back
    dg = dog((ox, -5.8, 0.16), mat('dogfur', (0.55, 0.38, 0.22), 0.8), math.pi)
    walker = cyl((ox + 0.6, -6.0, 0.8), 0.2, 1.3, tm)
    for o, dy in ((dg, 0), (walker, -0.3)):
        x0 = o.location.x
        key(o, 'scale', F(77.0), (0.001,)*3); key(o, 'scale', F(77.13), (1,1,1))
        key(o, 'location', F(77.13), (x0, -5.9 + dy, o.location.z)); key(o, 'location', F(78.0), (x0 - 7, -6.5 + dy, o.location.z))
        key(o, 'location', F(78.8), (x0, -5.9 + dy, o.location.z)); key(o, 'scale', F(78.8), (1,1,1)); key(o, 'scale', F(79.1), (0.001,)*3)
    # "no one entered": red scan frame round the door
    rm = emat('scanred', (1.0, 0.08, 0.05), 0); mkey(rm, F(80.3), 0); mkey(rm, F(80.8), 10); mkey(rm, F(82.6), 4); mkey(rm, F(83.0), 12)
    for zz in (0.05, 2.6): box((ox, -4.6, zz), (2.0, 0.05, 0.07), rm)
    for xx in (-1.0, 1.0): box((ox + xx, -4.6, 1.32), (0.07, 0.05, 2.6), rm)
    camera('C6', t0, t1, (ox - 1.2, -29, 7.5), (ox + 0.4, -22.5, 6.6), (ox + 0.8, -4, 5.6), (ox + 0.8, -4, 5.2), 30)

def s7(ox=600):
    t0, t1 = SHOTS[6][:2]
    wall = mat('wallw', (0.28, 0.2, 0.15), 0.9)
    box((ox, 2, 2.5), (10, 0.2, 5), wall); box((ox, 0, -0.05), (10, 6, 0.1), mat('floor2', (0.2, 0.17, 0.14), 0.7))
    box((ox, 0.6, 0.45), (5, 2.6, 0.9), mat('table', (0.3, 0.16, 0.08), 0.5))       # low table
    # shrine on the wall shelf
    gold = mat('gold', (0.9, 0.6, 0.2), 0.3, metal=1)
    box((ox - 1.6, 1.6, 1.6), (1.6, 0.7, 0.08), gold)
    for x in (-0.65, 0.65): cyl((ox - 1.6 + x, 1.6, 2.2), 0.05, 1.1, gold)
    box((ox - 1.6, 1.6, 2.8), (1.6, 0.7, 0.1), gold)
    sph((ox - 1.6, 1.6, 3.05), 0.45, gold).scale = (1, 0.8, 0.7)
    flame = emat('flame', (1.0, 0.55, 0.12), 25)
    for x in (-0.4, 0.4):
        cyl((ox - 1.6 + x, 1.35, 1.7), 0.09, 0.08, mat('clay', (0.5, 0.25, 0.1), 0.8))
        f = sph((ox - 1.6 + x, 1.35, 1.82), 0.05, flame); f.scale = (1, 1, 2.0)
        light_point((ox - 1.6 + x, 1.3, 1.95), 25, (1.0, 0.6, 0.25), 0.05)
    # 11 diaries drop into a stack
    cols = [(0.45, 0.08, 0.06), (0.1, 0.15, 0.35), (0.12, 0.25, 0.12), (0.4, 0.3, 0.08), (0.06, 0.06, 0.06)]
    rnd = random.Random(5)
    for i in range(11):
        z = 0.97 + i*0.15; d = diary((ox + 0.6, 0.6, z), cols[i % 5], rot=(0, 0, rnd.uniform(-0.15, 0.15)))
        t = 85.58 + i*0.09
        key(d, 'location', F(t) - 1, (ox + 0.6, 0.6, z + 6)); key(d, 'location', F(t) + 3, (ox + 0.6, 0.6, z))
    # open diary with lines being written
    pg = mat('paper', (0.85, 0.8, 0.68), 0.9)
    for sx in (-0.55, 0.55): box((ox - 1.0 + sx, 0.0, 0.92), (1.05, 1.4, 0.03), pg)
    box((ox - 1.0, 0.0, 0.905), (2.25, 1.5, 0.02), mat('cov7', (0.45, 0.08, 0.06), 0.55))
    ink = emat('ink', (1.0, 0.45, 0.1), 6)
    times = [91.85, 92.97, 94.04, 94.84, 95.92, 96.86, 98.04, 98.62, 99.88, 100.42, 101.63, 102.94]
    for k, t in enumerate(times):
        side = -0.55 if k < 6 else 0.55; row = k % 6
        ln = box((ox - 1.0 + side, 0.5 - row*0.2, 0.94), (0.8, 0.04, 0.01), ink)
        key(ln, 'scale', F(t) - 1, (0.001, 0.04, 0.01)); key(ln, 'scale', F(t) + 6, (0.8, 0.04, 0.01))
        ln.hide_render = True; ln.keyframe_insert('hide_render', frame=0); ln.hide_render = False; ln.keyframe_insert('hide_render', frame=F(t))
    light_area((ox + 2, -3, 4), 4, 250, (1.0, 0.85, 0.7)); aim(bpy.context.object, (ox, 0.5, 1))
    c, tg = camera('C7', t0, t1, (ox + 3.5, -5.5, 3.0), (ox - 0.4, -2.6, 4.6), (ox - 0.4, 1.0, 1.6), (ox - 0.4, 0.3, 0.9), 28)
    campath(c, [(90.6, (ox + 1.8, -3.8, 2.6))]); campath(tg, [(90.6, (ox - 0.2, 0.5, 1.2))])

def s8(ox=700):
    t0, t1 = SHOTS[7][:2]
    box((ox, 0, -0.05), (6, 6, 0.1), mat('table2', (0.12, 0.07, 0.04), 0.5))
    pg = mat('paper', (0.85, 0.8, 0.68), 0.9)
    for sx, rz in ((-0.55, 0.06), (0.55, -0.06)): box((ox + sx, 0, 0.02), (1.05, 1.4, 0.02), pg, rot=(0, rz, 0))
    ink = emat('ink8', (1.0, 0.45, 0.1), 3)
    for k in range(12):
        side = -0.55 if k < 6 else 0.55; box((ox + side, 0.5 - (k % 6)*0.2, 0.04), (0.8, 0.035, 0.01), ink)
    rope = emat('rope', (1.0, 0.7, 0.35), 5)
    a = torus((ox - 0.12, -0.6, 1.0), 0.35, 0.035, rope, (math.radians(90), 0, 0))
    b = torus((ox + 0.12, -0.6, 1.0), 0.35, 0.035, rope, (math.radians(90), math.radians(90), 0))
    move(a, 111.8, 113.0, (ox - 0.12, -0.6, 1.0), (ox - 0.8, -0.6, 1.0)); move(b, 111.8, 113.0, (ox + 0.12, -0.6, 1.0), (ox + 0.8, -0.6, 1.0))
    for m, base in ((rope, 5), (ink, 3)):
        mkey(m, F(106.1), base); mkey(m, F(114.9), base); mkey(m, F(115.4), base*2.2); mkey(m, F(116.2), 0.2)
    L = light_area((ox, -2, 3), 3, 160, (1.0, 0.85, 0.7)); aim(L, (ox, 0, 0))
    key(L.data, 'energy', F(114.9), 160); key(L.data, 'energy', F(116.2), 5)
    camera('C8', t0, t1, (ox, -4.2, 2.4), (ox, -3.0, 1.9), (ox, 0, 0.5), (ox, 0, 0.6), 32)

def build():
    s = setup(DUR)
    for f in (s1, s2, s3, s4, s5, s6, s7, s8): f()
    return s

if __name__ == '__main__':
    run(build, SHOTS, WORK + '/p1')
