#debug 
def pr(*a):
	#return
	for x in a: print x,
	print

def solve():
	pass
	
import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	pr(f.readline().strip())
	rt = solve()
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	#print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()