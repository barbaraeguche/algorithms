import heapq as hq

class Solution:
	def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
		adjacency = defaultdict(list)
		
		# build an adjacency list
		for u, v, w in edges:
			adjacency[u].append((w, v))
			adjacency[v].append((w, u))
		
		treeMap, minheap = {}, []
		
		treeMap[0] = [0, 0]  # start from 0
		for wei, dest in adjacency[0]:
			hq.heappush(minheap, (wei, 0, dest))
		
		while minheap:
			w, u, v = hq.heappop(minheap)
			
			# found a minimal spanner
			if v in treeMap:
				continue
			
			# mark the minimal spanner
			treeMap[v] = [u, w]
			
			for wei, dest in adjacency[v]:
				if not dest in treeMap:
					hq.heappush(minheap, (wei, v, dest))
		
		minSpan = 0
		
		# check connectivity
		for i in range(n):
			if not i in treeMap:
				return -1
			minSpan += treeMap[i][1]
		
		return minSpan
	