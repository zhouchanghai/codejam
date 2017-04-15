#debug 
def pr(*a):
	#return
	for x in a: print x,
	print

#breadth first search
def solve(hd0,ad0,hk0,ak0,b,d):
	step = 0
	stats = [(hd0,ad0,hk0,ak0)]
	all = set(stats)
	while 1:
		nextStat = set()
		step += 1
		for hd,ad,hk,ak in stats:
			if hk-ad <= 0:
				return step
			nextStat.add((hd0-ak,ad,hk,ak)) #c
			nextStat.add((hd-ak, ad, hk-ad, ak)) #a
			if b > 0:
				nextStat.add((hd-ak, ad+b, hk, ak)) #b
			if d > 0 and ak > 0:
				ak = max(ak-d, 0)
				nextStat.add((hd-ak, ad, hk, ak)) #d
		stats = set()
		for t in nextStat:
			if t[0] <= 0:
				continue
			if t not in all:
				all.add(t)
				stats.add(t)
		if not stats:
			return "IMPOSSIBLE"

import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	hd,ad,hk,ak,b,d = [int(x) for x in f.readline().strip().split()]
	rt = solve(hd,ad,hk,ak,b,d)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()