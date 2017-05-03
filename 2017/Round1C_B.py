#debug 
def pr(*a):
	#return
	for x in a: print x,
	print

#Implementation of the offcial analysis.
def solve(ac,aj,cs,js):
	if ac+aj==0:
		return 2
	events = []
	ctime, jtime = 0, 0
	for s,e in cs:
		events.append((s,e,'c'))
		ctime += e-s
	for s,e in js:
		events.append((s,e,'j'))
		jtime += e-s
	events.sort()
	events.append((events[0][0]+1440, events[0][1]+1440, events[0][2]))

	intervals = []
	for i in range(1, len(events)):
		pre = events[i-1]
		cur = events[i]
		time = cur[0] - pre[1]
		if cur[2]==pre[2]=='c':
			intervals.append((time, 'c'))
		elif cur[2]==pre[2]=='j':
			intervals.append((time, 'j'))
		else:
			intervals.append((time, 'x'))
	intervals.sort()

	#Assume the intervals are assigned to the third person
	exchanges = 2*(ac+aj)
	#Then replace the third person with C/J
	for length, type in intervals:
		if type=='c': 
			if ctime+length <= 720:
				ctime += length
				exchanges -= 2
		elif type=='j':
			if jtime+length <= 720:
				jtime += length
				exchanges -= 2
		else: #type=='x'
			exchanges -= 1
	return exchanges
	
import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	ac, aj = f.readline().strip().split()
	ac,aj = int(ac), int(aj)
	cs, js = [], []
	for i in range(ac):
		s,e = f.readline().strip().split()
		s,e = int(s), int(e)
		cs.append((s,e))
	for i in range(aj):
		s,e = f.readline().strip().split()
		s,e = int(s), int(e)
		js.append((s,e))
	rt = solve(ac,aj,cs,js)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()