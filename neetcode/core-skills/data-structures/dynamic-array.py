class DynamicArray:
	
	def __init__(self, capacity: int):
		self.count = 0
		self.capacity = capacity
		# nothing in the array
		self.nums = [0] * self.capacity
	
	def get(self, i: int) -> int:
		return self.nums[i]
	
	def set(self, i: int, n: int) -> None:
		self.nums[i] = n
	
	def pushback(self, n: int) -> None:
		# allocate new memory
		if self.count == self.capacity:
			self.resize()
		
		self.nums[self.count] = n
		self.count += 1
	
	def popback(self) -> int:
		# array will never be empty as per restrictions
		last = self.nums[self.count - 1]
		self.count -= 1
		
		return last
	
	def resize(self) -> None:
		# amortization
		self.capacity = self.count * 2
		array = [0] * self.capacity
		
		for i, num in enumerate(self.nums):
			array[i] = num
		
		self.nums = array
	
	def getSize(self) -> int:
		return self.count
	
	def getCapacity(self) -> int:
		return self.capacity
	