#debug 
def pr(*a):
	return
	for x in a: print x,
	print

def solve(N, V, X, rcs):
	EPS = 1E-10
	if len(rcs)==1:
		if rcs[0][1] != X: return "IMPOSSIBLE"
		return V/rcs[0][0]
	if len(rcs)==2:
		if (X-rcs[0][1])*(X-rcs[1][1]) > 0: return "IMPOSSIBLE"
		r0, r1 = rcs[0][0], rcs[1][0]
		a0 = r0*(rcs[0][1] - X)
		a1 = r1*(rcs[1][1] - X)
		if abs(a0) < EPS and abs(a1) < EPS:
			return V/(r0+r1)
		elif abs(a0) < EPS:
			return V/r0
		elif abs(a1) < EPS:
			return V/r1
		pr(a0, a1)
		pr(a0, a1, r0, r1*a0/a1)
		t0 = V/(r0 - r1*a0/a1)
		t1 = -a0*t0/a1
		return max(t0, t1)
	
import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	N, V, X = [s for s in f.readline().strip().split()]
	N, V, X = int(N), float(V), float(X)
	rcs = []
	for i in range(N):
		rcs.append([float(s) for s in f.readline().strip().split()])
	pr(N,V,X)
	pr(rcs)
	rt = solve(N,V,X,rcs)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()