#debug 
def pr(*a):
	#return
	for x in a: print x,
	print
	
def firstDiff(A,B):
	for i in xrange(len(A)):
		if A[i] != '?' and B[i] != '?' and A[i] != B[i]:
			return i
	return -1

#iDiff is the first diff position
#ai and bi are the chars at position iDiff, ai > bi
def makePair(A, B, iDiff, ai, bi):
	a = list(A)
	b = list(B)
	for i in range(len(A)):
		if i < iDiff:
			if A[i] == '?' and B[i] == '?':
				a[i] = '0'
				b[i] = '0'
			elif A[i] == '?':
				a[i] = B[i]
			elif B[i] == '?':
				b[i] = A[i]
		if i == iDiff:
			a[i] = ai
			b[i] = bi
		if i > iDiff:
			if A[i] == '?':
				a[i] = '0'
			if B[i] == '?':
				b[i] = '9'
	a = "".join(a)
	b = "".join(b)
	return abs(int(a)-int(b)), a, b
	
def solve(C,J):
	iDiff = firstDiff(C, J)
	if iDiff < 0:
		triple = makePair(C,J,1000,'','')
		return triple[1]+" "+triple[2]
	
	triple = (10**19, '', '')
	
	#make C larger
	if C[iDiff] > J[iDiff]:
		tmp = makePair(C, J, iDiff, C[iDiff], J[iDiff])
		triple = min(tmp, triple)
	else:
		for i in range(iDiff):
			if C[i] == '?' and J[i] == '?':
				tmp = makePair(C, J, i, '1', '0')
				triple = min(tmp, triple)
			elif C[i] == '?' and J[i] != '9':
				tmp = makePair(C, J, i, chr(ord(J[i])+1), J[i])
				triple = min(tmp, triple)
			elif J[i] == '?' and C[i] != '0':
				tmp = makePair(C, J, i, C[i], chr(ord(C[i])-1))
				triple = min(tmp, triple)

	#make J larger
	if C[iDiff] < J[iDiff]:
		tmp = makePair(J, C, iDiff, J[iDiff], C[iDiff])
		tmp = (tmp[0], tmp[2], tmp[1])
		triple = min(tmp, triple)
	else:
		for i in range(iDiff):
			if C[i] == '?' and J[i] == '?':
				tmp = makePair(J, C, i, '1', '0')
				tmp = (tmp[0], tmp[2], tmp[1])
				triple = min(tmp, triple)
			elif C[i] == '?' and J[i] != '0':
				tmp = makePair(J, C, i, J[i], chr(ord(J[i])-1))
				tmp = (tmp[0], tmp[2], tmp[1])
				triple = min(tmp, triple)
			elif J[i] == '?' and C[i] != '9':
				tmp = makePair(J, C, i, chr(ord(C[i])+1), C[i])
				tmp = (tmp[0], tmp[2], tmp[1])
				triple = min(tmp, triple)
	return triple[1] + " " + triple[2]
	
'''
#brute force 
def all(S):
	ret = [""]
	for c in S:
		tmp = []
		for pre in ret:
			if c=='?':
				for i in "0123456789":
					tmp.append(pre+i)
			else:
				tmp.append(pre+c)
		ret = tmp
	return ret
	
def bruteForce(C,J):
	a = all(C)
	b = all(J)
	pair, diff = None, 100000
	for x in a:
		for y in b:
			d = abs(int(x)-int(y))
			if d < diff:
				pair = (x,y)
				diff = d
			elif d == diff:
				pair = min((x,y), pair)
	return pair[0]+" "+pair[1]
'''

import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	A,B = f.readline().strip().split()
	rt = solve(A,B)
	pr(A)
	pr(B)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()
