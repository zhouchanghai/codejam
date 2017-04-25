#debug 
def pr(*a):
	#return
	for x in a: print x,
	print

def solve(D,N,h):
	t = 0
	for k,s in h:
		t = max((D-k)/s, t)
	return D/t
	
import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	D,N = f.readline().strip().split()
	D,N = int(D), int(N)
	horses = []
	for i in range(N):
		k,s = f.readline().strip().split()
		k,s = float(k), float(s)
		horses.append((k,s))
	rt = solve(D,N,horses)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()