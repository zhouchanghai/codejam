
def count(s):
	rc,pc,sc = 0,0,0
	for c in s:
		if c=="R": rc += 1
		elif c=="P": pc += 1
		elif c=="S": sc += 1
	return rc,pc,sc

def generate():
	r = ["R"]
	p = ["P"]
	s = ["S"]
	for i in range(12):
		#R <= R,S; P <= P,R; S <= P,S;
		R = r[-1]+s[-1] if r[-1]<s[-1] else s[-1]+r[-1]
		P = p[-1]+r[-1] if p[-1]<r[-1] else r[-1]+p[-1]
		S = p[-1]+s[-1] if p[-1]<s[-1] else s[-1]+p[-1]
		r.append(R)
		p.append(P)
		s.append(S)
	return r,p,s

rs,ps,ss = generate()

def solve(N,R,P,S):
	ret = "ZZZ"
	if count(rs[N]) == (R,P,S):
		ret = rs[N]
	if count(ps[N]) == (R,P,S) and ps[N] < ret:
		ret = ps[N]
	if count(ss[N]) == (R,P,S) and ss[N] < ret:
		ret = ss[N]
	if ret[0] == "Z":
		return "IMPOSSIBLE"
	return ret
	
import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	N,R,P,S = [int(x) for x in f.readline().strip().split()]
	rt = solve(N,R,P,S)
	print >>out, "Case #%d: %s"%(tc, str(rt))
out.close()