#debug 
def pr(*a):
	return
	for x in a: print x,
	print

def solve(B,N,M):
	if N <= B: return N
	right = max(M)*N
	left = 1
	
	while left+1 < right:
		mid = (left+right)/2
		processing = 0
		for i in range(B):
			processing += mid//M[i] + 1
		pr("time processing", mid, processing)
		if processing < N:
			left = mid
		else:
			right = mid
	assert left+1 == right
	pr("left mid right", left, mid, right)
	
	processing = 0
	newprocess = []
	for i in range(B):
		processing += right//M[i] + 1
		if right%M[i] == 0:
			newprocess.append(i+1)
	newprocess.sort()
	pr("processing newprocess", processing, newprocess)
	return newprocess[N-(processing-len(newprocess))-1]
	
import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	B, N = f.readline().strip().split()
	B, N = int(B), int(N)
	M = [int(x) for x in f.readline().strip().split()]
	pr(B,N)
	pr(M)
	rt = solve(B,N,M)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()