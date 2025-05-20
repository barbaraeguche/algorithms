from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
	def __init__(self) -> None:
		self.stack: list[T] = []
		self.top = None
		
	def push(self, item: T) -> None:
		self.stack.append(item)
		self.top = item
	
	def pop(self) -> str | T:
		if self.isEmpty():
			return "Stack is empty"
		
		popped = self.stack.pop()
		self.top = None if self.isEmpty() else self.stack[-1]
		
		return popped
	
	def peek(self) -> str | T:
		if self.isEmpty():
			return "Stack is empty"
		return self.top
	
	def isEmpty(self) -> bool:
		return not bool(self.stack)
	
	
if __name__ == "__main__":
	# initialize the stack
	stack = Stack()
	
	# push to stack
	stack.push("1")
	stack.push(1.0)
	stack.push(5)
	stack.push(True)
	stack.push([])
	
	# peek
	print(f"Peek: {stack.peek()}")
	# empty check
	print(f"Empty: {stack.isEmpty()}")
	
	# pop
	print(f"Pop: {stack.pop()}")
	# peek
	print(f"Peek: {stack.peek()}")
	
	# pop
	print(f"Pop: {stack.pop()}")
	# peek
	print(f"Peek: {stack.peek()}")
	
	# pop
	print(f"Pop: {stack.pop()}")
	# peek
	print(f"Peek: {stack.peek()}")
	