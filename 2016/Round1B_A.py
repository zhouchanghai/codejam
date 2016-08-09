#debug 
def pr(*a):
	return
	for x in a: print x,
	print

def solve(S):
	count = [0]*10
	key = {}
	atoi = {"ZERO":0, "ONE":1, "TWO":2, "THREE":3, "FOUR":4, 
	"FIVE":5, "SIX":6, "SEVEN":7, "EIGHT":8, "NINE":9}
	for number in atoi:
		for c in number:
			key[c] = key.get(c, 0) + 1
	chars = {}
	for c in S:
		chars[c] = chars.get(c, 0) + 1

	while atoi:
		for uniq in key:
			if key[uniq]==1:
				break
		for number in atoi:
			if uniq in number:
				break
		cnt = chars.get(uniq, 0)
		count[atoi[number]] += cnt
		for c in number:
			chars[c] = chars.get(c,0) - cnt
			key[c] -= 1
		del atoi[number]
	
	ret = ""
	for i in range(10):
		ret += str(i) * count[i]
	return ret


import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	S = f.readline().strip()
	rt = solve(S)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()