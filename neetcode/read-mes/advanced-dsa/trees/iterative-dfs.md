## iterative dfs
the recursive approach for performing dfs is trivial. so sometimes the interviewer may ask you to code up the iterative 
solution, which can be a lot trickier. it is good to know in situations like these.

recursion makes use of a stack under the hood. in the iterative version, we will declare our own stack(s) to perform the 
same operations.

### implementation
if we declare our own stacks, we can intelligently push to the stack, taking into consideration the order in which we 
need to print/pop our nodes. recall that there are three main ways to traverse a tree:
- inorder
- preorder
- postorder

### inorder
recall that inorder traversal involves visiting:
- the left child (including its entire subtree).
- then the current node.
- and finally, the right child (including its entire subtree).

we will declare a `curr` pointer, which will point to the current node that we are processing. Once our `curr` pointer 
points at a node, we will add it to the stack. after this, we will update our `curr` pointer to be `curr.left`. if our 
`curr` points to `null`, we can pop from the `stack`, print the node's value and traverse the right subtree.

```python
def inorder(root):
  curr, stack = root, []

  while curr or stack:
    if curr:
      stack.append(curr)
      curr = curr.left
    else:
      curr = stack.pop()
      print(curr.val)
      curr = curr.right
```

### preorder
recall that preorder traversal involves visiting:
- the current node.
- then the left subtree.
- and finally the right subtree.

to implement this iterative, we will still loop through the left pointers of the tree. however, we will print the value 
of the node before traversing the left pointer. we will also push the right pointer to the stack before traversing the 
left pointer, rather than inserting the current node.

this way, we can print the current node before traversing the left subtree, and then traverse the right subtree.
```python
def preorder(root):
  curr, stack = root, []
  
  while curr or stack:
    if curr:
      print(curr.val)
      if curr.right:
        stack.append(curr.right)
      curr = curr.left
    else:
      curr = stack.pop()
```

### postorder
postorder traversal deals with traversing the left child, right child and then the root. this one is more complicated 
than the previous two.

we will be making use of two stacks. in this case, we will have a `visit` stack and another stack called `stack`.

the `visit` and `stack` stacks will always be the same size. the `stack` stack will be used to store the nodes we are 
currently processing, while the `visit` stack will be used to keep track of whether we have previously visited the 
corresponding node in `stack` or not.

we can then run a while loop, i.e. `while stack is not null` (since our `visited` and `stack` is the exact same size). 
using this, we will pop from our `stack` and `visited`. if our `curr` is not `null`, we check if we have visited it.
```python
def postorder(root):
  visit, stack = [False], [root]
  
  while stack:
    curr, visited = stack.pop(), visit.pop()
    
    if curr:
      if visited:
        print(curr.val)
      else:
        stack.append(curr)
        visit.append(True)
        
        stack.append(curr.right)
        visit.append(False)
        
        stack.append(curr.left)
        visit.append(False)
```

### time complexities
if `n` is the number of nodes, and we are doing $`O(1)`$ work at each node, then the time complexity is $`O(n)`$. this 
is also be referred to as $`O(h)`$ where `h` is the height of the tree.

### space complexities
the space complexity is $`O(n)`$ where in the worst case, we have all the nodes in the stack.