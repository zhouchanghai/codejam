#debug 
def pr(*a):
	#return
	for x in a: print x,
	print
	
def split(size):
	half = size // 2
	if size % 2 == 0:
		return (half, half - 1)
	else:
		return (half, half)

def solve(n, k):
	que = Queue.PriorityQueue() # element: -size
	que.put(-n)
	for i in range(k-1):
		size = -que.get()
		splits = split(size)
		for newSize in splits:
			if newSize > 0:
				que.put(-newSize)

	size = -que.get()
	splits = split(size)
	return "%d %d"%splits
	
import sys, Queue
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	N, K = f.readline().strip().split()
	N, K = int(N), int(K)
	rt = solve(N, K)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()