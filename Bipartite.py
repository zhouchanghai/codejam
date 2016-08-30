#Bipartite graph
class Bipartite:
	def __init__(self):
		'''public properties'''
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