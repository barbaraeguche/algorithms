class Node:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class LinkedList:
	
	def __init__(self):
		# dummy node for easier insertion
		self.head = Node(-1)
		self.tail = self.head
	
	def get(self, index: int) -> int:
		idx, curr = 0, self.head.next
		
		while curr:
			if idx == index:
				return curr.val
			
			idx += 1
			curr = curr.next
		
		return -1  # index out of bounds
	
	def insertHead(self, val: int) -> None:
		newHead = Node(val)
		
		newHead.next = self.head.next
		self.head.next = newHead
		
		# first node to be inserted
		if not newHead.next:
			self.tail = newHead
	
	def insertTail(self, val: int) -> None:
		newTail = Node(val)
		
		self.tail.next = newTail
		self.tail = newTail
		
	def remove(self, index: int) -> bool:
		idx, curr = 0, self.head
		
		while idx < index and curr:
			idx += 1
			curr = curr.next
		
		if curr and curr.next:
			# if removing the last node in the list
			if curr.next == self.tail:
				self.tail = curr
				
			curr.next = curr.next.next
			return True
		
		return False
	
	def getValues(self) -> List[int]:
		curr = self.head.next
		values = []
		
		while curr:
			values.append(curr.val)
			curr = curr.next
		
		return values
		