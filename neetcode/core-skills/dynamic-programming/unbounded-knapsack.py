class Solution:
	def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
		n, m = len(profit), capacity
		dp = [0] * (m + 1)
		
		for i in range(n):
			dpCopy = dp[:]  # a copy of the current dp
			
			for j in range(1, m + 1):
				skip = dpCopy[j]  # not take this profit
				
				include = 0
				# if the current capacity can carry the i-th
				# weight, how much profit can we make?
				if j >= weight[i]:
					include = profit[i] + dpCopy[j - weight[i]]
				
				# keep track of the current max profit
				dpCopy[j] = max(include, skip)
			
			# update the table
			dp = dpCopy
		
		return dp[m]

# tc: O(n * m)
# sc: O(m)