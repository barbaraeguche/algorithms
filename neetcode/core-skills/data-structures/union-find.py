class UnionFind:
	
	def __init__(self, n: int):
		self.components = n
		self.parent = {}
		self.rank = {}
		
		for i in range(n):
			self.parent[i] = i
			self.rank[i] = 0
	
	def find(self, x: int) -> int:
		if x != self.parent[x]:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]
	
	def isSameComponent(self, x: int, y: int) -> bool:
		return self.find(x) == self.find(y)
	
	def union(self, x: int, y: int) -> bool:
		px, py = self.find(x), self.find(y)
		
		if px == py:
			return False
		
		if self.rank[px] < self.rank[py]:
			self.parent[px] = py
		elif self.rank[py] < self.rank[px]:
			self.parent[py] = px
		else:
			self.parent[px] = py
			self.rank[py] += 1
		
		self.components -= 1
		return True
	
	def getNumComponents(self) -> int:
		return self.components
	