from typing import TypeVar, Generic

T = TypeVar('T')

class Queue(Generic[T]):
	def __init__(self) -> None:
		self.queue: list[T] = []
		self.first = None
		
	def enqueue(self, item: T) -> None:
		self.queue.append(item)
	
	def dequeue(self) -> None:
		if self.isEmpty():
			return "Queue is empty"
		
		dequeued = self.queue[0]
		self.queue = self.queue[1:]
		
		self.first = None if self.isEmpty() else self.queue[0]
		return dequeued
	
	def front(self) -> str | T:
		if self.isEmpty():
			return "Queue is empty"
		
		self.first = self.queue[0]
		return self.first
	
	def isEmpty(self) -> bool:
		return not bool(self.queue)
	
	
if __name__ == "__main__":
	queue = Queue()
	
	# push to stack
	queue.enqueue("1")
	queue.enqueue(1.0)
	queue.enqueue(5)
	queue.enqueue(True)
	queue.enqueue([])
	
	# peek
	print(f"Front: {queue.front()}")
	# empty check
	print(f"Empty: {queue.isEmpty()}")
	
	# pop
	print(f"Dequeue: {queue.dequeue()}")
	# peek
	print(f"Front: {queue.front()}")
	
	# pop
	print(f"Dequeue: {queue.dequeue()}")
	# peek
	print(f"Front: {queue.front()}")
	
	# pop
	print(f"Dequeue: {queue.dequeue()}")
	# peek
	print(f"Front: {queue.front()}")
	