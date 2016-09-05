#debug 
def pr(*a):
	return
	for x in a: print x,
	print

import Queue
def solve(P):
	q = Queue.PriorityQueue()
	remain = sum(P)
	for i in range(len(P)):
		q.put((-P[i], chr(ord('A')+i)))
	order = []
	
	while not q.empty():
		#evacuate one person
		head = q.get()
		order.append(head[1])
		if head[0] < -1:
			q.put((head[0]+1, head[1]))
		remain -= 1
		
		if -head[0]*2 > remain and remain > 0:
			head = q.get()
			#if the remain has an absolute majority, evacuate another one
			if -head[0]*2 > remain:
				order[-1] += head[1]
				remain -= 1
				if head[0] < -1:
					q.put((head[0]+1, head[1]))
			else:
				q.put(head)
	return " ".join(order)
	
import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	N = int(f.readline().strip())
	P = [int(x) for x in f.readline().strip().split()]
	rt = solve(P)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()