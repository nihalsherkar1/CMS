import json, re, sys
p = sys.argv[1]
W = json.load(open(f'/tmp/work/{p}_words.json')); H = open(f'/tmp/work/{p}_hing.txt').read().split()
DUR = {'p1': 116.28, 'p2': 84.384}[p]
ORANGE, YEL, WHITE, RED, CYAN = '&H00008AFF&', '&H004AE2FF&', '&H00FFFFFF&', '&H00303BFF&', '&H00FFD84F&'
KEY = set('11 1 2018 das gyaarah paanch pandrah assi lalit jacky cctv diaries qatl zinda bargad shared psychosis haadsa sagaai sawaal aatma aadesh tape patti stool taar rotiyan hoobahoo kram tapasya bhram tantrik baba 2007 hazaar saat narayani gurcharan burari rooh yaqeen'.split())
def ts(t):
    t = max(0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f'{h}:{m:02d}:{s:05.2f}'
head = f'''[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Inter Display Black,74,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,-1,0,0,0,100,100,0,0,1,6,3,5,80,80,0,1
Style: Lab,Inter Display Black,90,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,-1,0,0,0,100,100,1,0,1,6,4,8,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''
ev = []
# ---- captions: chunks of <=4 words / ~22 chars, break after punctuation
chunks, cur = [], []
for i, h in enumerate(H):
    cur.append(i)
    n = len(' '.join(re.sub(r'\.\.\.', '', H[j]) for j in cur))
    if re.search(r'[.,?:]$', h) or len(cur) >= 4 or n > 20: chunks.append(cur); cur = []
if cur: chunks.append(cur)
def clean(h): return re.sub(r'\.\.\.$|[.,:]$', '', h)
for ci, ch in enumerate(chunks):
    nxt = W[chunks[ci + 1][0]]['start'] if ci + 1 < len(chunks) else DUR
    end_chunk = min(nxt, W[ch[-1]]['end'] + 0.6)
    for k, i in enumerate(ch):
        a = W[i]['start']; b = W[ch[k + 1]]['start'] if k + 1 < len(ch) else end_chunk
        parts = []
        for j in ch:
            word = clean(H[j]); base = ORANGE if re.sub(r'[^a-z0-9]', '', word.lower()) in KEY else WHITE
            if j == i: parts.append(r'{\c' + (ORANGE if base == ORANGE else YEL) + r'\fscx112\fscy112}' + word + r'{\fscx100\fscy100\c' + WHITE + '}')
            elif j < i or True: parts.append(r'{\c' + base + '}' + word)
        fade = r'\fad(80,0)' if k == 0 else ''
        ev.append(f'Dialogue: 1,{ts(a)},{ts(b)},Cap,,0,0,0,,{{\\pos(540,1370){fade}}}' + r' \h'.join(parts))
# ---- big labels per shot
L = {
'p1': [((0.00, 6.04), [('11 LIVES', 0.00, ORANGE, 150), ('ONE NIGHT', 1.86, WHITE, 90), ('DOOR OPEN', 4.67, WHITE, 70)]),
       ((6.04, 24.38), [('1 JULY 2018', 6.04, ORANGE, 110), ('7:15 AM', 9.10, WHITE, 90), ('BURARI, DELHI', 10.84, WHITE, 64), ('SHOP SHUT', 20.80, RED, 72)]),
       ((24.38, 40.37), [('10 FOUND', 31.06, ORANGE, 140), ('BLINDFOLDED', 33.70, WHITE, 66), ('MOUTHS TAPED', 35.52, WHITE, 66), ('HANDS TIED', 38.84, WHITE, 66)]),
       ((40.37, 55.85), [('NARAYANI DEVI, 80', 41.31, WHITE, 78), ('ONLY SURVIVOR: JACKY', 50.14, ORANGE, 70), ('YOUNGEST: 15', 54.50, WHITE, 78)]),
       ((55.85, 61.01), [('MURDER?', 57.36, RED, 150)]),
       ((61.01, 83.49), [('● CCTV  30 JUNE 2018', 62.47, RED, 54), ('10:00 PM · 5 STOOLS', 65.28, WHITE, 62), ('10:15 PM · WIRES', 69.38, WHITE, 62),
                         ('10:40 PM · 20 ROTIS', 74.02, WHITE, 62), ('10:57 PM · DOG WALK', 77.13, WHITE, 62), ('NO ONE ENTERED', 80.79, ORANGE, 96)]),
       ((83.49, 106.08), [('11 DIARIES', 85.58, ORANGE, 130), ('2007 → 2018', 87.66, WHITE, 90), ('EVERY STEP WRITTEN', 92.97, WHITE, 64), ('EXACTLY AS WRITTEN', 102.94, ORANGE, 64)]),
       ((106.08, 116.28), [('THEY THOUGHT', 113.45, WHITE, 84), ("THEY'D SURVIVE", 114.97, ORANGE, 110)])],
'p2': [((0.0, 6.79), [('FATHER DIES', 5.48, WHITE, 84)]),
       ((6.79, 18.90), [('"FATHER\'S SPIRIT"', 9.08, ORANGE, 92), ('ORDERS', 13.03, WHITE, 90), ('WHOLE FAMILY OBEYED', 16.96, WHITE, 62)]),
       ((18.90, 23.35), [('BUSINESS GREW', 18.90, WHITE, 84), ('BELIEF DEEPENED', 21.42, ORANGE, 84)]),
       ((23.35, 30.27), [('FINAL ORDER', 24.00, WHITE, 80), ('BARGAD TAPASYA', 25.10, ORANGE, 100), ('LIKE BANYAN ROOTS', 27.64, WHITE, 66)]),
       ((30.27, 48.32), [('CBI-CFSL PSYCHOLOGICAL AUTOPSY', 31.10, WHITE, 46), ('SHARED PSYCHOSIS', 33.64, RED, 96), ('NOT SUICIDE', 42.20, WHITE, 70),
                         ('ACCIDENT DURING RITUAL', 44.28, ORANGE, 70), ('NO TANTRIK FOUND', 46.24, WHITE, 64)]),
       ((48.32, 62.11), [('UNANSWERED', 48.78, WHITE, 90), ('ENGAGED 17 JUNE 2018', 53.50, ORANGE, 70), ('MURDER?', 61.22, RED, 120)]),
       ((62.11, 75.43), [('11', 63.89, ORANGE, 200), ('NEVER QUESTIONED', 73.74, WHITE, 90)]),
       ((75.43, 84.384), [('COMMENT ↓', 80.01, ORANGE, 66), ('FOLLOW +', 83.44, WHITE, 60)])]}
for (s0, s1), labs in L[p]:
    y = 290
    y = 290; an, x = 8, 540
    if p == 'p1' and 61 < s0 < 62: an, x = 7, 50
    for txt, t, col, size in labs:
        pop = r'\fscx10\fscy10\t(0,120,\fscx115\fscy115)\t(120,200,\fscx100\fscy100)'
        ev.append(f'Dialogue: 2,{ts(t)},{ts(s1 - 0.02)},Lab,,0,0,0,,{{\\an{an}\\pos({x},{y})\\fs{size}\\c{col}{pop}\\fad(0,120)}}{txt}')
        y += int(size * 1.18) + 8
open(f'/tmp/work/ov/{p}.ass', 'w').write(head + '\n'.join(ev) + '\n')
print(p, len(ev), 'events')
