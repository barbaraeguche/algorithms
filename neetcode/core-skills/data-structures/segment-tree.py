class SegmentNode:
	def __init__(self, total=0, L=0, R=0):
		self.rangeSum = total
		self.L, self.R = L, R
		self.left = self.right = None
	
	def build(self, nums, L, R):
		# base case
		if L == R:
			return SegmentNode(nums[L], L, R)
		
		M = (L + R) // 2
		
		# form the tree
		root = SegmentNode(0, L, R)
		root.left = self.build(nums, L, M)
		root.right = self.build(nums, M + 1, R)
		
		# store the range sum
		root.rangeSum = root.left.rangeSum + root.right.rangeSum
		return root
	
	def update(self, idx, val):
		# at a given index
		if self.L == self.R:
			self.rangeSum = val
			return
		
		M = (self.L + self.R) // 2
		
		if idx <= M:
			self.left.update(idx, val)
		else:
			self.right.update(idx, val)
		
		# update the range sum
		self.rangeSum = self.left.rangeSum + self.right.rangeSum
	
	def rangeQuery(self, L, R):
		# found the range
		if self.L == L and self.R == R:
			return self.rangeSum
		
		M = (self.L + self.R) // 2
		
		if L > M:
			return self.right.rangeQuery(L, R)
		elif R <= M:
			return self.left.rangeQuery(L, R)
		else:
			return self.left.rangeQuery(L, M) + self.right.rangeQuery(M + 1, R)

class SegmentTree:
	
	def __init__(self, nums: List[int]):
		self.root = SegmentNode()
		# build the segment tree
		self.root = self.root.build(nums, 0, len(nums) - 1)
	
	def update(self, index: int, val: int) -> None:
		self.root.update(index, val)
	
	def query(self, L: int, R: int) -> int:
		return self.root.rangeQuery(L, R)
