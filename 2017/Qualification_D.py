#debug 
def pr(*a):
	return
	for x in a: print x,
	print

#see util/Bipartite.py
import Bipartite

def solve(N, M, grid):
	#put x: one row/column can have at most 1 x
	rows = [i for i in range(N)]
	cols = [i for i in range(N)]
	for i in range(N):
		for j in range(N):
			if grid[i][j] in "ox":
				rows[i] = -1
				cols[j] = -1
	rows = filter(lambda x: x>=0, rows)
	cols = filter(lambda x: x>=0, cols)
	assert len(rows) == len(cols)
	xs = set()
	for rc in zip(rows, cols):
		xs.add(rc)
		
	#put +: one diagonal can have at most 1 +
	#two types of diagonal, from left to right up (const r+c) or down(const r-c)
	rpc = set()
	rmc = set()
	bi = Bipartite()
	for i in range(2*N-1):
		rpc.add(i)
	for i in range(-N+1, N):
		rmc.add(i)
	assert len(rpc) == 2*N - 1
	assert len(rmc) == 2*N - 1
	for i in range(N):
		for j in range(N):
			if grid[i][j] in "o+":
				assert i+j in rpc
				assert i-j in rmc
				rpc.remove(i+j)
				rmc.remove(i-j)
	for i in range(N):
		for j in range(N):
			if i+j in rpc and i-j in rmc:
				bi.addEdge(i+j, i-j)
	match = BipartiteMatch(bi)
	match.match()
	ps = set()
	for ia, ib in enumerate(match.aMatch):
		if ib >= 0:
			rpc = bi.a[ia]
			rmc = bi.b[ib]
			r = (rpc+rmc)/2
			c = (rpc-rmc)/2
			ps.add((r,c))
	
	score = 0
	ret = []
	for i in range(N):
		for j in range(N):
			type = 0 #x 1, + 2, o 3
			if grid[i][j] in "xo":
				score += 1
				type += 1
			if grid[i][j] in "+o":
				score += 1
				type += 2
			add = False
			if (i, j) in xs:
				score += 1
				type += 1
				add = True
			if (i, j) in ps:
				score += 1
				type += 2
				add = True
			if add:
				ret.append("%s %d %d"%(".x+o"[type], i+1, j+1))
	ret.insert(0, "%d %d"%(score, len(ret)))
	return "\n".join(ret)
	
import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	N, M = f.readline().strip().split()
	N, M = int(N), int(M)
	grid = [["."] * N for i in range(N)]
	for i in range(M):
		model, x, y = f.readline().strip().split()
		grid[int(x)-1][int(y)-1] = model
	rt = solve(N, M, grid)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()