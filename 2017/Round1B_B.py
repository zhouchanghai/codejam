#debug 
def pr(*a):
	#return
	for x in a: print x,
	print

#I believe the code is right. But it can't pass the B-large-practice.in
def match(a, b):
	m = {"R":"YGB", "O":"B", "Y":"RVB", "G":"R", "B":"ROY", "V":"Y"}
	return b in m[a]

def nextPos(n, i):
	i += 2
	if i in (n, n+1):
		return 1
	return i

def simple(rs,ys,bs):
	arr = [(len(rs), rs), (len(ys), ys), (len(bs), bs)]
	total = arr[0][0] + arr[1][0] + arr[2][0]
	arr.sort(reverse=True)
	if 2*arr[0][0] > total:
		return "IMPOSSIBLE"
	ret = [0] * total
	pos = 0
	for t in arr:
		for color in t[1]:
			ret[pos] = color
			pos = nextPos(total, pos)
	ret = "".join(ret)

	assert len(ret) == N
	count = {}
	for i in range(N):
		assert match(ret[i], ret[(i+1)%N])
		count[ret[i]] = count.get(ret[i], 0) + 1
	assert R == count.get("R", 0)
	assert O == count.get("O", 0)
	assert Y == count.get("Y", 0)
	assert G == count.get("G", 0)
	assert B == count.get("B", 0)
	assert V == count.get("V", 0)
	return ret

def solve():
	if O+G+V == 0:
		return simple(["R"]*R, ["Y"]*Y, ["B"]*B)
	else:
		if R < G or Y < V or B < O:
			return "IMPOSSIBLE"
		r2 = R-G
		y2 = Y-V
		b2 = B-O
		if (r2==0 and G>0) or (y2==0 and V>0) or (b2==0 and O>0):
			flag = 0
			if G > 0:
				flag += 1
				ret = "RG" * G
			if V > 0:
				flag +=1
				ret = "YV" * V
			if O > 0:
				flag += 1
				ret = "BO" * O
			if flag > 1:
				return "IMPOSSIBLE"
			else:
				return ret
		rs = ["R"] * r2
		ys = ["Y"] * y2
		bs = ["B"] * b2
		if r2 > 0:
			rs[0] = "RG"*G + "R"
		if y2 > 0:
			ys[0] = "YV"*V + "Y"
		if b2 > 0:
			bs[0] = "BO"*O + "B"
		return simple(rs, ys, bs)
	
import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	line = f.readline().strip()
	N,R,O,Y,G,B,V = [int(x) for x in line.split()]
	pr("R", R, "O", O, "Y", Y, "G", G, "B", B, "V", V)
	rt = solve()
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()