import heapq as hq

class Solution:
	def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
		adjacency = defaultdict(list)
		
		# build an adjacency list
		for u, v, w in edges:
			adjacency[u].append((w, v))
		
		pathMap, minheap = {}, [(0, src)]
		
		while minheap:
			w, u = hq.heappop(minheap)
			
			# found a shorter path
			if u in pathMap:
				continue
			
			# mark the shortest path
			pathMap[u] = w
			
			for wei, dest in adjacency[u]:
				if not dest in pathMap:
					hq.heappush(minheap, (w + wei, dest))
		
		for i in range(n):
			if not i in pathMap:
				pathMap[i] = -1
		
		return pathMap
