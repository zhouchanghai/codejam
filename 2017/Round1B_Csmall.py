#debug 
def pr(*a):
	#return
	for x in a: print x,
	print

def solve():
	arr = []
	arr.append((0,es[0][0], es[0][1])) #(timestamp, remain E, S)
	for i in range(1, N):
		tmp = []
		d = D[i-1][i]
		for t,e,s in arr:
			if e >= d:
				tmp.append((t+float(d)/s, e-d, s))
		tmp.sort()
		#choose the first arrived, and switch the horse
		tmp.append((tmp[0][0], es[i][0], es[i][1]))
		arr = tmp
	return arr[0][0]
	
import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	N,Q = f.readline().strip().split()
	N,Q = int(N), int(Q)
	es = []
	for i in range(N):
		e,s = f.readline().strip().split()
		e,s = int(e), int(s)
		es.append((e,s))
	D = []
	for i in range(N):
		D.append([int(x) for x in f.readline().strip().split()])
	f.readline() #the only query
	rt = solve()
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()