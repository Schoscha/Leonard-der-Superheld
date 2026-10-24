# Synthesizes the SFX + music bed track for "Leonard erwacht" (39 s, 48 kHz stereo)
import sys, wave, numpy as np
SR=48000; DUR=39.0; N=int(SR*DUR)
L=np.zeros(N); R=np.zeros(N)
rng=np.random.default_rng(7)
def t(n): return np.arange(n)/SR
def add(sig, at, gain=1.0, pan=0.0):
    i=int(at*SR); n=min(len(sig), N-i)
    if n<=0: return
    L[i:i+n]+=sig[:n]*gain*np.sqrt((1-pan)/2)*1.414
    R[i:i+n]+=sig[:n]*gain*np.sqrt((1+pan)/2)*1.414
def env(n, a, r):
    e=np.ones(n); na=int(a*SR); nr=int(r*SR)
    if na: e[:na]=np.linspace(0,1,na)
    if nr: e[-nr:]*=np.linspace(1,0,nr)
    return e
def lp(x, a):  # one-pole lowpass, a in (0,1)
    y=np.empty_like(x); s=0.0
    for i in range(len(x)): s+=a*(x[i]-s); y[i]=s
    return y
def bandnoise(n, lo_a, hi_a):
    w=rng.standard_normal(n); return lp(w,hi_a)-lp(w,lo_a)

# 1) Alarm clock ringing 0.2-2.2 s (bell partials, 22 Hz hammer rattle)
n=int(2.0*SR); tt=t(n)
bell=sum(np.sin(2*np.pi*f*tt)*g for f,g in [(1850,1),(2790,.5),(4100,.25)])
ham=(0.5+0.5*np.sign(np.sin(2*np.pi*22*tt)))*np.exp(-((tt*22)%1)*3)
gate=(np.sin(2*np.pi*1.6*tt)>-0.3).astype(float)
add(bell*ham*gate*env(n,.01,.3), 0.2, 0.10, pan=0.5)

# 2) Soft birds in the morning 0-9 s
for k in range(9):
    at=0.6+k*1.0+rng.uniform(0,.5); n=int(.18*SR); tt=t(n)
    f=3200+1200*np.sin(2*np.pi*12*tt); ph=2*np.pi*np.cumsum(f)/SR
    add(np.sin(ph)*np.sin(np.pi*tt/.18)**2, at, 0.03, pan=-0.6)

# 3) Tension music bed 9.5-26.3 s: low drone + pulsing bass that accelerates
start,end=9.5,26.3; n=int((end-start)*SR); tt=t(n)
drone=(np.sin(2*np.pi*55*tt)+.5*np.sin(2*np.pi*82.4*tt)+.3*np.sin(2*np.pi*110.5*tt))
add(drone*env(n,3,0.05)*np.linspace(.5,1,n), start, 0.06)
bt=start; k=0
while bt<end-0.1:
    prog=(bt-start)/(end-start); per=0.75-0.5*prog   # pulse speeds up
    m=int(.22*SR); mt=t(m)
    kick=np.sin(2*np.pi*(45+60*np.exp(-mt*30))*mt)*np.exp(-mt*14)
    add(kick, bt, 0.25+0.35*prog); bt+=per; k+=1

# 4) Whip whoosh at the cut to the wardrobe/suit (≈19.3 s)
def whoosh(dur, pan0, pan1, bright=.15):
    n=int(dur*SR); tt=t(n)
    x=bandnoise(n,.01,bright)*np.sin(np.pi*tt/dur)**2
    return x/np.abs(x).max(), n
w,n=whoosh(.55,-1,1)
for side,g in ((L,np.linspace(1,.2,n)),(R,np.linspace(.2,1,n))):
    i=int(19.05*SR); side[i:i+n]+=w*g*0.5

# 5) Spin: repeated swirling whooshes 22.0-26.3 accelerating + shimmer
at=22.0; d=.6
while at<26.0:
    w,n=whoosh(d,0,0,bright=.25)
    pan=np.sin(at*7)
    add(w, at, 0.28, pan=float(pan)); at+=d*0.7; d=max(.22,d*0.85)
n=int(4.4*SR); tt=t(n)
sh=np.zeros(n)
for _ in range(120):
    f=rng.uniform(2500,7000); s=int(rng.uniform(0,n-SR*.2)); m=int(.15*SR)
    sh[s:s+m]+=np.sin(2*np.pi*f*t(m))*np.exp(-t(m)*30)
add(sh*np.linspace(.3,1,n), 21.9, 0.05)

# 6) Riser 21.6-26.3 (rising sine sweep + noise)
n=int(4.7*SR); tt=t(n); f=200+1600*(tt/4.7)**2
riser=np.sin(2*np.pi*np.cumsum(f)/SR)*.5+bandnoise(n,.02,.3)*1.5
add(riser*(tt/4.7)**2, 21.6, 0.12)

# 7) Transformation impact 26.3 s: boom + bright crash
n=int(2.5*SR); tt=t(n)
boom=np.sin(2*np.pi*(40+90*np.exp(-tt*8))*tt)*np.exp(-tt*2.2)
crash=bandnoise(n,.2,.9)*np.exp(-tt*2.5)
add(boom, 26.3, 0.9); add(crash/np.abs(crash).max(), 26.3, 0.18)
# magic chime arpeggio after impact
for k,fr in enumerate([1046.5,1318.5,1568,2093]):
    m=int(1.2*SR); mt=t(m)
    add((np.sin(2*np.pi*fr*mt)+.3*np.sin(2*np.pi*fr*2*mt))*np.exp(-mt*3), 26.45+k*0.09, 0.07, pan=-.4+k*.27)

# 8) Mirror reveal stinger ≈32.0 s: low hit + dissonant strings-ish swell
n=int(3.0*SR); tt=t(n)
hit=np.sin(2*np.pi*(50+50*np.exp(-tt*10))*tt)*np.exp(-tt*2.8)
add(hit, 32.0, 0.7)
sw=sum(np.sin(2*np.pi*f*tt+np.sin(2*np.pi*5*tt)*.3) for f in (220,233.1,329.6))
add(sw*env(n,.05,1.2)*np.exp(-tt*.6), 32.0, 0.05)

# 9) Heroic ending 35.5-39: rising major chord swell + final hit
n=int(3.5*SR); tt=t(n)
ch=sum(np.sin(2*np.pi*f*tt)+.4*np.sin(2*np.pi*2*f*tt) for f in (196,246.9,293.7,392))
add(ch*env(n,2.0,1.2), 35.5, 0.05)
m=int(1.8*SR); mt=t(m)
add(np.sin(2*np.pi*(55+70*np.exp(-mt*9))*mt)*np.exp(-mt*2.5), 37.4, 0.6)

st=np.stack([L,R],1); st/=max(1.0,np.abs(st).max()/0.95)
with wave.open(sys.argv[1],"wb") as wf:
    wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR)
    wf.writeframes((st*32767).astype(np.int16).tobytes())
print("ok")
