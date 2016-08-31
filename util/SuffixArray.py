class SaComparator:
	def __init__(self, group, t):
		self.group = group
		self.t = t

	def __call__(self, i, j):
		group = self.group
		t = self.t 
		if group[i] != group[j]:
			return group[i] - group[j]
		else:
			return group[i+t] - group[j+t]
			
def strCmp(a,i,b,j,size):
	n = 0
	while i<len(a) and j<len(b) and n<size:
		if a[i] < b[j]:
			return -1
		if a[i] > b[j]:
			return 1
		i += 1
		j += 1
		n += 1
	if n==size:
		return 0
	if i < len(a):
		return 1
	if j < len(b):
		return -1

class SuffixArray:
	def __init__(self, S):
		'''Build the suffix array in O(N * logN * logN) time using the Manber & Myers algorithm.'''
		
		n = len(S)
		sa = [0] * (n+1)
		group = [0] * (n+1)

		for i in xrange(n):
			sa[i] = i
			group[i] = ord(S[i])
		sa[-1] = n
		group[-1] = -1

		t = 1
		while 1:
			comp = SaComparator(group, t)
			sa.sort(comp)
			newGroup = [0] * (n+1)
			for i in xrange(1, n+1):
				if comp(sa[i-1], sa[i]) != 0:
					newGroup[sa[i]] = newGroup[sa[i-1]] + 1
				else:
					newGroup[sa[i]] = newGroup[sa[i-1]]
			group = newGroup
			t *= 2
			if t >= n: break
		self.S = S
		self.sa = sa
		self.rank = group
		self.lcp = None

	def getSA(self):
		'''Get the suffix array with length N+1.

		sa[0] is always the empty string S[N:]
		'''
		return self.sa
	
	def getRank(self):
		'''Get the rank array with length N+1.

		The rank (rank[N]) of empty string S[N:] is always 0.
		'''
		return self.rank

	def contains(self, needle):
		'''Return True if needle is a substr of S, False otherwise.

		The time complexity is O(|needle| * log|S|).
		'''
		pos = self.findInsertPos(needle)
		if pos > len(self.S):
			return False
		posInS = self.sa[pos]
		i = 0
		while i<len(needle) and posInS < len(self.S):
			if needle[i] != self.S[posInS]:
				return False
			i += 1
			posInS += 1
		return i == len(needle)

	def getLCP(self):
		'''Return the Longest Common Prefix Array with length N+1.

		LCP[i] is the Longest Common Prefix between S[sa[i]:] and S[sa[i-1]:].
		'''
		if self.lcp:
			return self.lcp
		n = len(self.S)
		lcp = [0] * (n+1)
		common = 0
		for i in xrange(n):
			j = self.sa[self.rank[i] - 1]
			if common > 0:
				common -= 1
			while j+common < n and i+common < n and self.S[j+common] == self.S[i+common]:
				common += 1
			lcp[self.rank[i]] = common
		self.lcp = lcp
		return lcp
	
	def findInsertPos(self, needle):
		'''Return the first insert position of needle in the array.

		The time complexity is O(|needle| * log|S|).
		'''
		if not needle: return 0
		a, b = 0, len(self.S)+1
		#assert S[sa[a]:] < needle and S[sa[b]:] >= needle
		while b - a > 1:
			c = (a+b)//2
			if strCmp(self.S, self.sa[c], needle, 0, len(needle)) < 0:
				a = c
			else:
				b = c
		return b

		
if __name__ == "__main__":
	import sys
	if len(sys.argv) > 1:
		hay = sys.argv[1]
	else:
		hay = "mississipi"
	sa = SuffixArray(hay)
	print "the suffix array and lcp:"
	print "sa", sa.getSA()
	print "lcp", sa.getLCP()
	print "i sa[i] substr lcp[i]"
	for i in range(len(hay)+1):
		sai, lcpi = sa.getSA()[i], sa.getLCP()[i]
		print i, sai, hay[sai:], lcpi
	
	if len(sys.argv) > 2:
		needle = sys.argv[2]
		print hay, "contains", needle, ":", sa.contains(needle)