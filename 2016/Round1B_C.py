#debug 
def pr(*a):
	#return
	for x in a: print x,
	print

'''
For each pair A,B draw an edge between A-B.
Find miminum edges to cover all vertex, and then other edges are fake.
|edge cover| + |bipartite match| = |V|
see https://en.wikipedia.org/wiki/Edge_cover
'''
def solve(pairs):
	graph = Bipartite()
	for a,b in pairs:
		graph.addEdge(a,b)
	match = BipartiteMatch(graph).match()
	cover = len(graph.a)+len(graph.b)-match
	return len(pairs)-cover
	
	
class Bipartite:
	def __init__(self):
		#convert a object to index
		self.aIdx = {}
		#convert b object to index
		self.bIdx = {}
		#a objects
		self.a = []
		#b objects
		self.b = []
		self.aAdjs = []
		self.bAdjs = []
	
	def addEdge(self, a, b):
		if a not in self.aIdx:
			self.aIdx[a] = len(self.a)
			self.a.append(a)
			self.aAdjs.append([])
		if b not in self.bIdx:
			self.bIdx[b] = len(self.b)
			self.b.append(b)
			self.bAdjs.append([])
		self.aAdjs[self.aIdx[a]].append(self.bIdx[b])
		self.bAdjs[self.bIdx[b]].append(self.aIdx[a])
		
class BipartiteMatch:
	def __init__(self, bipartite):
		self.graph = bipartite
	
	def dfs(self, aIdx):
		if self.visited[aIdx]: return False
		self.visited[aIdx] = True
		for bIdx in self.graph.aAdjs[aIdx]:
			if self.bMatch[bIdx] < 0 or self.dfs(self.bMatch[bIdx]):
				self.aMatch[aIdx] = bIdx
				self.bMatch[bIdx] = aIdx
				return True
		return False
	
	def match(self):
		self.aMatch = [-1] * len(self.graph.a)
		self.bMatch = [-1] * len(self.graph.b)
		size = 0
		for start in range(len(self.graph.a)):
			self.visited = [0] * len(self.graph.a)
			if self.dfs(start):
				size += 1
		return size

import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())
print T
for tc in range(1, T+1):
	n = int(f.readline().strip())
	pairs = []
	for i in range(n):
		A,B = f.readline().strip().split()
		pairs.append((A,B))
	rt = solve(pairs)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()