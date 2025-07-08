class Graph:
	
	def __init__(self):
		self.graph = defaultdict(list)
	
	def addEdge(self, src: int, dst: int) -> None:
		self.graph[src].append(dst)
		
		# add the destination to graph
		if not dst in self.graph:
			self.graph[dst] = []
	
	def removeEdge(self, src: int, dst: int) -> bool:
		# if any node not in graph
		if not (src in self.graph and dst in self.graph):
			return False
		
		# remove the edge
		del self.graph[src]
		return True
	
	def hasPath(self, src: int, dst: int) -> bool:
		def dfs(source, destination, seen):
			# cannot be re-traversed
			if source in seen:
				return False
			# reached destination
			if source == destination:
				return True
			
			# add visited vertex to set
			seen.add(source)
			
			# dfs on its neighbours
			for neigh in self.graph.get(source, []):
				if dfs(neigh, destination, seen):
					return True
			
			return False
		
		return dfs(src, dst, set())
