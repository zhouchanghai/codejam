#debug 
def pr(*a):
	return
	for x in a: print x,
	print
	
def tieVote(all):
	probability  = {0:1.0}
	for pY in all:
		tmp = {}
		for extraY in probability :
			pExtraY = probability[extraY]
			tmp[extraY+1] = tmp.get(extraY+1, 0) + pExtraY*pY
			tmp[extraY-1] = tmp.get(extraY-1, 0) + pExtraY*(1-pY)
		probability = tmp
	return probability[0]

# O(K*K*K)
def solve(P, K):
	P.sort()
	N = len(P)
	if K==N:
		return tieVote(P)
	ret = 0
	for left in range(K+1):
		all = P[:left] + P[N-(K-left):]
		ret = max(ret, tieVote(all))
	return ret

import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	N, K = f.readline().strip().split()
	N, K = int(N), int(K)
	P = [float(x) for x in f.readline().strip().split()]
	rt = solve(P, K)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()