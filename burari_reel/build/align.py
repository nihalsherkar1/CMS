import re, json, sys, subprocess, numpy as np, uroman
U=uroman.Uroman()
name=sys.argv[1]
txt=open(f'{name}.txt').read()
dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'{name}.wav']))
out=subprocess.run(['ffmpeg','-i',f'{name}.wav','-af','silencedetect=n=-35dB:d=0.18','-f','null','-'],capture_output=True,text=True).stderr
ss=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',out)]; se=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',out)]
# speech segments
segs=[]; t=0.0
for a,b in zip(ss,se):
    if a-t>0.05: segs.append((t,a))
    t=b
if dur-t>0.1: segs.append((t,dur))
# phrases split at punctuation
phr=[p.strip() for p in re.split(r'(?<=[।,?:])\s+|\.\.\.\s*|\.\s+',txt.replace('\n',' ')) if p.strip()]
SP={'11':'gyaarah','1':'ek','2018':'dohazaaraatthaarah','CCTV':'seeseeteevee','CBI':'seebeeaai'}
def rom(w):
    w2=w.strip('।,?:.!'); r=SP.get(w2) or U.romanize_string(w); return re.sub(r'[^a-z0-9]','',r.lower())
def w_of(p): return [w for w in p.split() if re.sub(r'[।,?:.!]','',w)]
pw=[sum(len(rom(w))+1 for w in w_of(p)) for p in phr]
segd=[b-a for a,b in segs]
rate=sum(pw)/sum(segd)
# word-level DP: each speech segment gets a contiguous run of >=1 words
W=[]; P=[]
for p in phr:
    ws=w_of(p)
    for n,w in enumerate(ws): W.append(w); P.append(n==len(ws)-1)
L=[len(rom(w))+1 for w in W]; cum=np.concatenate([[0],np.cumsum(L)])
N,M=len(W),len(segs); rate=cum[-1]/sum(segd)
INF=1e18; D=np.full((M+1,N+1),INF); B=np.zeros((M+1,N+1),int); D[0,0]=0
for j in range(1,M+1):
    for i in range(1,N+1):
        pen=0 if (i==N or P[i-1]) else 0.6
        for k in range(max(0,i-30),i):
            if D[j-1,k]>=INF: continue
            exp=(cum[i]-cum[k])/rate; c=D[j-1,k]+(np.log(exp/segd[j-1]))**2+pen
            if c<D[j,i]: D[j,i]=c; B[j,i]=k
i=N; assign=[]
for j in range(M,0,-1):
    k=B[j,i]; assign.append((j-1,k,i)); i=k
assign.reverse()
words=[]
for j,k,i in assign:
    a,b=segs[j]; tot=cum[i]-cum[k]; t=a
    for w,l in zip(W[k:i],L[k:i]):
        c=re.sub(r'[।,?:.!]','',w); d=(b-a)*l/tot
        words.append(dict(word=c,roman=U.romanize_string(c),start=round(t,3),end=round(t+d,3))); t+=d
    print(f'{a:6.2f}-{b:6.2f} ({b-a:4.2f}s exp {tot/rate:4.2f}) | '+' '.join(W[k:i]))
json.dump(words,open(f'{name}_words.json','w'),ensure_ascii=False,indent=0)
print(len(phr),'phrases',len(segs),'segs',len(words),'words')
