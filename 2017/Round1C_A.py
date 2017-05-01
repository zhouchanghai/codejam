#debug 
def pr(*a):
	#return
	for x in a: print x,
	print
import math

#The method is O(N*N*logN), enough for the large data set. 
#For better performance, see the analysis. 
def solve(N,K,rh):
	rh.sort(reverse=True)
	ret = 0
	for i in range(0, N-K+1):
		r, h = rh[i]
		area = math.pi*r*r + 2*math.pi*r*h
		side = map(lambda t: 2*math.pi*t[0]*t[1], rh[i+1:])
		side.sort(reverse=True)
		for j in range(K-1):
			area += side[j]
		ret = max(area, ret)
	return ret
	
import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	N, K = f.readline().strip().split()
	N, K = int(N), int(K)
	rh = []
	for i in range(N):
		r,h = f.readline().strip().split()
		r,h = int(r), int(h)
		rh.append((r,h))
	rt = solve(N,K,rh)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()