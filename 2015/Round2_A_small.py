#debug 
def pr(*a):
	return
	for x in a: print x,
	print
	
def next(R,C,g, i,j,d):
	if d=='^':
		while i > 0:
			i -= 1
			if g[i][j] != '.': return (i,j)
		return -2
	if d=="<":
		while j > 0:
			j -= 1
			if g[i][j] !='.': return (i,j)
		return -2
	if d=="v":
		while i < R-1:
			i += 1
			if g[i][j] !='.': return (i,j)
		return -2
	if d==">":
		while j < C-1:
			j += 1
			if g[i][j] !='.': return (i,j)
		return -2
	return -1
	

def solve(R,C,g):
	to = [[0]*C for i in range(R)]
	change = 0
	for i in range(R):
		for j in range(C):
			to[i][j] = next(R,C,g, i,j, g[i][j])
			if to[i][j] == -2:
				for d in "^v<>":
					if next(R,C,g,i,j,d) != -2:
						change += 1
						break
				else:
					return "IMPOSSIBLE"
	return change
	
import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	R,C = [int(s) for s in f.readline().strip().split()]
	pr(R,C)
	g = []
	for i in range(R):
		g.append(f.readline().strip())
	pr(g)
	rt = solve(R,C,g)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()