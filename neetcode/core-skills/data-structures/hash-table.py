class HashNode:
	def __init__(self, key=0, val=0):
		self.key = key
		self.val = val
		self.next = None

class HashTable:
	
	def __init__(self, capacity: int):
		self.size = 0
		self.capacity = capacity
		self.hashTable = [None] * self.capacity
	
	def hashKey(self, key: int) -> int:
		return key % self.capacity
	
	def insert(self, key: int, value: int) -> None:
		idx = self.hashKey(key)
		node = self.hashTable[idx]
		
		newNode = HashNode(key, value)
		
		# first node at hash
		if not node:
			self.hashTable[idx] = newNode
		else:
			while node:
				# change value if key already in hash
				if node.key == key:
					node.val = value
					return
				
				prev, node = node, node.next
			
			# add to the end of list
			prev.next = newNode
		
		# increment the number of nodes
		self.size += 1
		
		# resize the hash table
		if (self.size / self.capacity) >= 0.5:
			self.resize()
	
	def get(self, key: int) -> int:
		idx = self.hashKey(key)
		node = self.hashTable[idx]
		
		while node:
			# return the value of the key
			if node.key == key:
				return node.val
			node = node.next
		
		return -1
	
	def remove(self, key: int) -> bool:
		idx = self.hashKey(key)
		node = self.hashTable[idx]
		
		prev = None
		
		while node:
			if node.key == key:
				if prev:  # remove current node
					prev.next = node.next
				else:  # if only one node
					self.hashTable[idx] = node.next
				
				# decrement the number of nodes
				self.size -= 1
				return True
			
			prev, node = node, node.next
		
		return False
	
	def getSize(self) -> int:
		return self.size
	
	def getCapacity(self) -> int:
		return self.capacity
	
	def resize(self) -> None:
		newCapacity = self.capacity * 2
		newHashTable = [None] * newCapacity
		
		for idx in range(newCapacity):
			if idx >= self.capacity:
				break
			
			# nodes at current index
			node = self.hashTable[idx]
			
			head = HashNode(-1, -1)
			curr = head
			
			# copy into new map
			while node:
				# create new node
				curr.next = HashNode(node.key, node.val)
				
				curr = curr.next
				node = node.next
			
			# add to new hash table
			newHashTable[idx] = head.next
			
		# update capacity and hash table
		self.capacity = newCapacity
		self.hashTable = newHashTable
