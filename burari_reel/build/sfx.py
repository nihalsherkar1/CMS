import numpy as np, soundfile as sf, sys, json, subprocess
from scipy.signal import butter, sosfilt
SR = 48000
p = sys.argv[1]
DUR = {'p1': 116.28, 'p2': 84.384}[p]
CUTS = {'p1': [6.04, 24.38, 40.37, 55.85, 61.01, 83.49, 106.08], 'p2': [6.79, 18.90, 23.35, 30.27, 48.32, 62.11, 75.43]}[p]
N = int(DUR * SR); t = np.arange(N) / SR; rng = np.random.default_rng(1)
def bp(x, lo, hi): return sosfilt(butter(2, [lo, hi], 'band', fs=SR, output='sos'), x)
def lp(x, f): return sosfilt(butter(2, f, 'low', fs=SR, output='sos'), x)
out = np.zeros(N)
# drone: low sines + filtered noise with slow LFO
drone = 0.5*np.sin(2*np.pi*55*t) + 0.3*np.sin(2*np.pi*82.4*t + 0.5) + 0.15*np.sin(2*np.pi*110.3*t)
drone *= 0.6 + 0.4*np.sin(2*np.pi*0.07*t)
drone += lp(rng.standard_normal(N), 300) * 0.8 * (0.6 + 0.4*np.sin(2*np.pi*0.11*t + 1))
out += drone * 0.25
# whoosh on each cut: band-passed noise sweep peaking at the cut
for c in CUTS:
    L = int(0.5 * SR); a = int((c - 0.4) * SR); n = rng.standard_normal(L)
    seg = np.zeros(L); steps = 20
    for k in range(steps):
        lo = 300 + 2500 * k / steps; s0, s1 = k*L//steps, (k+1)*L//steps
        seg[s0:s1] = bp(n, lo, lo*2.2)[s0:s1]
    env = np.concatenate([np.linspace(0, 1, int(0.4*SR))**2, np.linspace(1, 0, L - int(0.4*SR))**1.5])
    b = min(N, a + L); out[a:b] += (seg * env)[:b-a] * 2.2
# impact boom on key reveals
hits = {'p1': [0.0, 31.06, 57.36, 85.58, 114.97], 'p2': [1.10, 25.10, 33.64, 61.22, 63.89]}[p]
for h in hits:
    L = int(1.2*SR); a = int(h*SR); tt = np.arange(L)/SR
    boom = np.sin(2*np.pi*(60*np.exp(-tt*2) + 35)*tt) * np.exp(-tt*3.5)
    b = min(N, a + L); out[a:b] += boom[:b-a] * 1.4
if p == 'p1':   # clock ticks under CCTV shot
    for k in np.arange(61.5, 83.3, 1.0):
        a = int(k*SR); L = int(0.03*SR); out[a:a+L] += bp(rng.standard_normal(L), 2000, 6000) * np.exp(-np.arange(L)/300) * 1.5
if p == 'p2':   # rain under house shot
    a, b = int(62.11*SR), int(75.43*SR); r = bp(rng.standard_normal(b - a), 800, 7000) * 0.5
    fade = np.minimum(1, np.minimum(np.arange(b-a), np.arange(b-a)[::-1]) / SR / 0.6); out[a:b] += r * fade
# duck under voice
v, vsr = sf.read(f'/tmp/work/{p}.wav'); env = np.abs(v)
win = int(vsr*0.15); env = np.convolve(env, np.ones(win)/win, 'same'); env = np.interp(t, np.arange(len(env))/vsr, env)
active = env > 0.02; duck = np.where(active, 0.45, 1.0); duck = np.convolve(duck, np.ones(int(SR*0.1))/int(SR*0.1), 'same')
out *= duck
out /= np.max(np.abs(out)) + 1e-9
sf.write(f'/tmp/work/ov/{p}_sfx.wav', out.astype(np.float32), SR)
