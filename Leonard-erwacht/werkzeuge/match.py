import sys, subprocess, numpy as np
def frames(path, ss, t):
    cmd=["ffmpeg","-v","error","-ss",str(ss),"-i",path,"-t",str(t),"-vf","scale=160:90,format=gray","-f","rawvideo","-"]
    b=subprocess.run(cmd,capture_output=True).stdout
    return np.frombuffer(b,np.uint8).reshape(-1,90,160).astype(np.float32)
a,b=sys.argv[1],sys.argv[2]
A=frames(a,7.0,3.0); B=frames(b,0,3.0)
best=[]
for i in range(len(A)):
    for j in range(len(B)):
        best.append((np.mean((A[i]-B[j])**2),i,j))
best.sort()
print("A frames",len(A),"B frames",len(B))
for m,i,j in best[:8]:
    print(f"mse={m:7.1f}  A_t={7+i/24:.3f}s  B_t={j/24:.3f}s")
print("naive end/start mse", np.mean((A[-1]-B[0])**2))
