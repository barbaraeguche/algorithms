class Solution:
	def shortestPath(self, grid: List[List[int]]) -> int:
		rows, cols = len(grid), len(grid[0])
		directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
		
		path = 0
		seen, queue = {0, 0}, deque([(0, 0)])
		
		while queue:
			length = len(queue)
			
			for _ in range(length):
				nr, nc = queue.popleft()
				
				# bottom right reached
				if nr == rows - 1 and nc == cols - 1:
					return path
				
				for dr, dc in directions:
					row, col = nr + dr, nc + dc
					
					# within the grid range
					if (
						0 <= row < rows and
						0 <= col < cols and
						grid[row][col] == 0 and
						(row, col) not in seen
					):
						seen.add((row, col))
						queue.append((row, col))
			
			# increment for current batch of paths
			path += 1
		
		return -1
	