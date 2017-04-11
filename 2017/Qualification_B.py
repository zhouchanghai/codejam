#debug 
def pr(*a):
	#return
	for x in a: print x,
	print

'''
def isTidy(n):
	s = str(n)
	for i in range(1, len(s)):
		if s[i] < s[i-1]:
			return False
	return True

def solveNaive(n):
	while n >= 0:
		if isTidy(n):
			return n
		else:
			n -= 1
'''

def fill(a, start, x):
	for i in range(start, len(a)):
		a[i] = x

def solve(n):
	arr = [ch for ch in str(n)]
	for i in range(len(arr)):
		for d in "9876543210":
			fill(arr, i, d)
			if int("".join(arr)) <= n:
				break
	return int("".join(arr))

import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	n = int(f.readline().strip())
	rt = solve(n)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()