class MinHeap:
	
	def __init__(self):
		self.minHeap = [0]
	
	def push(self, val: int) -> None:
		length = len(self.minHeap)
		
		# add to heap
		self.minHeap.append(val)
		# percolate up
		self.pushHelper(length)
	
	def pop(self) -> int:
		if self.empty():
			return -1
		
		last = len(self.minHeap) - 1
		# percolate down
		return self.popHelper(last)
	
	def top(self) -> int:
		if self.empty():
			return -1
		return self.minHeap[1]
	
	def heapify(self, nums: List[int]) -> None:
		if len(nums) > 1:
			# 0-th position is moved to the end
			nums.append(nums[0])
			nums[0] = 0  # default back to zero
			
			self.minHeap = nums
			idx = (len(self.minHeap) - 1) // 2
			
			while idx > 0:
				# sort the tree
				self.orderHeap(idx)
				idx -= 1
	
	def empty(self) -> bool:
		return len(self.minHeap) == 1
	
	def pushHelper(self, idx: int) -> None:
		# while the new value is lesser than its parent
		while idx > 1 and self.minHeap[idx] < self.minHeap[idx // 2]:
			self.minHeap[idx // 2], self.minHeap[idx] = self.minHeap[idx], self.minHeap[idx // 2]
			idx //= 2
	
	def popHelper(self, last: int) -> int:
		idx, value = 1, self.minHeap[1]
		
		# swap with first node
		self.minHeap[idx] = self.minHeap[last]
		# remove from heap
		self.minHeap.pop()
		
		# sort the tree
		self.orderHeap(idx)
		
		# remove the smallest value
		return value
	
	def orderHeap(self, idx: int):
		left = idx * 2
		right = idx * 2 + 1
		
		while left < len(self.minHeap):
			# right child (if exist) is the smallest amongst the three
			if (
				right < len(self.minHeap) and
				self.minHeap[right] < self.minHeap[left] and
				self.minHeap[right] < self.minHeap[idx]
			):
				self.minHeap[idx], self.minHeap[right] = self.minHeap[right], self.minHeap[idx]
			
			# left child is the smallest
			elif self.minHeap[left] < self.minHeap[idx]:
				self.minHeap[idx], self.minHeap[left] = self.minHeap[left], self.minHeap[idx]
			
			# same value
			else:
				break
