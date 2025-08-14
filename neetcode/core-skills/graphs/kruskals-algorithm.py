import heapq as hq

class UnionFind:
	def __init__(self, n):
		self.parent = {}
		self.rank = {}
		
		for i in range(n):
			self.parent[i] = i
			self.rank[i] = 0
	
	def find(self, n):
		if n != self.parent[n]:
			self.parent[n] = self.find(self.parent[n])
		return self.parent[n]
	
	def union(self, n1, n2):
		p1, p2 = self.find(n1), self.find(n2)
		
		if p1 == p2:
			return False
		
		if self.rank[p1] < self.rank[p2]:
			self.parent[p1] = p2
		elif self.rank[p2] < self.rank[p1]:
			self.parent[p2] = p1
		else:
			self.parent[p1] = p2
			self.rank[p2] += 1
		
		return True

class Solution:
	def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
		minHeap = []
		for u, v, w in edges:
			hq.heappush(minHeap, (w, u, v))
		
		uf = UnionFind(n)
		weight, components = 0, n
		
		while minHeap and components > 1:
			w, u, v = hq.heappop(minHeap)
			
			if uf.union(u, v):
				weight += w
				components -= 1
		
		return weight if components == 1 else -1
