class TreeNode:
	def __init__(self, key=0, val=0, left=None, right=None):
		self.key = key
		self.val = val
		self.left = left
		self.right = right

class TreeMap:
	
	def __init__(self):
		self.root = None
		self.treeMap = {}
	
	def insert(self, key: int, val: int) -> None:
		node = TreeNode(key, val)
		
		# add to map
		self.treeMap[key] = node
		# add to tree
		self.root = self.addToTree(self.root, node)
	
	def get(self, key: int) -> int:
		if key in self.treeMap:
			return self.treeMap[key].val
		return -1
	
	def getMin(self) -> int:
		node = self.getMinNode(self.root)
		return node.val if node else -1
	
	def getMax(self) -> int:
		node = self.root
		
		# the largest key is always on the right
		while node and node.right:
			node = node.right
		return node.val if node else -1
	
	def remove(self, key: int) -> None:
		if key in self.treeMap:
			# remove from map
			del self.treeMap[key]
			# remove from the tree
			self.root = self.removeFromTree(self.root, key)
	
	def getInorderKeys(self) -> List[int]:
		inorder = []
		
		def dfs(node):
			if node:
				dfs(node.left)
				inorder.append(node.key)
				dfs(node.right)
		
		dfs(self.root)
		return inorder
	
	def addToTree(self, root, node):
		if not root:
			return node  # passing initialised node already
		
		if node.key < root.key:
			root.left = self.addToTree(root.left, node)
		elif node.key > root.key:
			root.right = self.addToTree(root.right, node)
		else:
			root.val = node.val  # update the value instead
		
		return root
	
	def removeFromTree(self, root, key):
		if not root:
			return root
		
		if key < root.key:
			root.left = self.removeFromTree(root.left, key)
		elif key > root.key:
			root.right = self.removeFromTree(root.right, key)
		else:
			if not root.left:
				return root.right
			if not root.right:
				return root.left
			
			minNode = self.getMinNode(root.right)
			
			# update key-value pair
			root.key, root.val = minNode.key, minNode.val
			root.right = self.removeFromTree(root.right, minNode.key)
		
		return root
	
	def getMinNode(self, root):
		node = root
		
		# the smallest node is always on the left
		while node and node.left:
			node = node.left
		return node
	