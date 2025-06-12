class Node:
	def __init__(self, val=0, prev=None, next=None):
		self.val = val
		self.prev = prev
		self.next = next

class Deque:
	
	def __init__(self):
		self.head, self.tail = Node(-1), Node(-1)
		# connect nodes
		self.head.next, self.tail.prev = self.tail, self.head
	
	def isEmpty(self) -> bool:
		return self.head.next == self.tail
	
	def append(self, value: int) -> None:
		node = Node(value)
		penultimate, tail = self.tail.prev, self.tail
		
		# connect nodes
		penultimate.next = tail.prev = node
		node.prev, node.next = penultimate, tail
	
	def appendleft(self, value: int) -> None:
		node = Node(value)
		head, nxt = self.head, self.head.next
		
		# connect nodes
		head.next = nxt.prev = node
		node.prev, node.next = head, nxt
	
	def pop(self) -> int:
		if self.isEmpty():
			return -1
		
		penultimate, tail = self.tail.prev, self.tail
		# connect nodes while removing the last
		penultimate.prev.next, tail.prev = tail, penultimate.prev
		
		return penultimate.val
	
	def popleft(self) -> int:
		if self.isEmpty():
			return -1
		
		head, nxt = self.head, self.head.next
		# connect nodes while removing the first
		head.next, nxt.next.prev = nxt.next, head
		
		return nxt.val
