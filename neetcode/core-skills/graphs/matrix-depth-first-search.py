class Solution:
	def countPaths(self, grid: List[List[int]]) -> int:
		rows, cols = len(grid), len(grid[0])
		
		def traversal(r, c, seen):
			# bottom right reached
			if r == rows - 1 and c == cols - 1:
				return 1 if grid[r][c] == 0 else 0
			
			# within bounds
			if not (
				0 <= r < rows and
				0 <= c < cols and
				grid[r][c] == 0 and
				(r, c) not in seen
			):
				return 0
			
			# add to visited path
			seen.add((r, c))
			# all possible other paths
			path = (
				traversal(r-1, c, seen) +
				traversal(r+1, c, seen) +
				traversal(r, c-1, seen) +
				traversal(r, c+1, seen)
			)
			
			# remove form visited path
			seen.remove((r, c))
			return path
		
		return traversal(0, 0, set())
