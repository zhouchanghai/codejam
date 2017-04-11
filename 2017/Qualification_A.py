#debug 
def pr(*a):
	#return
	for x in a: print x,
	print

def flip(x):
	if x=="+":
		return "-"
	else:
		return "+"

def solve(cakes, k):
	n = len(cakes)
	arr = [c for c in cakes]
	flips = 0
	for i in range(n-k+1):
		if arr[i] == "-":
			for j in range(k):
				arr[i+j] = flip(arr[i+j])
			flips += 1
	for i in range(n-k+1, n):
		if arr[i] == "-":
			return "IMPOSSIBLE"
	return flips
	
import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	cakes, k = f.readline().strip().split()
	k = int(k)
	rt = solve(cakes, k)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()