class Solution:
	def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
		incoming, adjacentList = [0] * n, defaultdict(list)
		
		# build an adjacent list
		for src, dest in edges:
			adjacentList[src].append(dest)
			# keep track of in-degree nodes
			incoming[dest] += 1
		
		queue = deque()
		
		# start with vertices that have no in-degree nodes
		for i in range(n):
			if incoming[i] == 0:
				queue.append(i)
		
		topologicalOrder = []
		
		while queue:
			node = queue.popleft()
			# add vertex to order
			topologicalOrder.append(node)
			
			for dest in adjacentList[node]:
				# remove the current incoming node
				incoming[dest] -= 1
				
				# if there are no in-degree nodes, add to queue
				if incoming[dest] == 0:
					queue.append(dest)
			
			# visited this node
			del adjacentList[node]
		
		# if a cycle was found
		if len(topologicalOrder) != n:
			return []
		
		return topologicalOrder