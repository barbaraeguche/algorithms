## segment tree
the structure of segment trees is one of the most complex among tree structures, but we will strive to simplify it as 
much as we can.

### motivation
suppose we were given a range of values. then, given a left and a right pointer that defines the range, we want to be 
able to calculate the sum of the range. this is the fundamental textbook problem behind segment trees, and this is what
we will be focusing on.

solving this using an array is trivial but to go through the range, in the worst case, takes $`O(n)`$ time. if we want to 
update a value in an array, it is done in $`O(1)`$ time. now, segment trees promise to implement both update and perform
queries in $`O(log(n))`$ time. though it adds more overhead to the update function, the tradeoff is that our search 
function will be much faster.

not too dissimilar to merge sort, the idea here is to break up the array into segments, by a branching factor of two to 
be more precise, and have each node represent a progressively smaller range. we break up the array into two equal halves, 
and each node represents a range (which are basically indices of arrays).

the visual below demonstrates how a segment tree is constructed using an array. the numbers in red represent the sum of 
the range at that given node. the numbers inside the node represent the range itself, inclusive of both numbers. the 
text in blue represents the formula for calculating the range.

### implementation
similar to heaps, segment trees can be constructed using arrays. recall that heaps are almost complete binary trees 
where every level is full except possibly the last level. however, segment trees have gaps in the last level, which 
makes them harder to be implemented with arrays. so, we will implement them using objects of a `SegmentTree` class, 
which can be conceptualized as nodes.

- #### segment tree constructor
we will need the following in our `SegmentTree` class constructor.

- `sum`, which will keep track of the sum at each node.
- `right` and `left` pointers to the right and the left child (similar to binary trees).
- at any given node, `L` and `R` denote the left and right boundaries of the contained range, respectively.
```python
class SegmentTree:
  def __init__(self, total, L, R):
    self.sum = total
    
    self.L, self.R = L, R
    self.left = self.right = None
```

### building the segment tree
given an array `nums` and `L` and `R`, we can take a recursive approach. at each level, we calculate `M`, which splits 
the current range in half, and builds the tree until we hit our base case, where `L == R`, i.e. the range gets exhausted.

to start off, we will initialize a `root` with a sum of `0`. we can then recursively calculate the sum at each node and
return the ultimate sum.
```python
def build(self, nums, L, R):
  if L == R:
    return SegmentTree(nums[L], L, R)
    
  M = (L + R) // 2
  root = SegmentTree(0, L, R)
  
  root.left = self.build(nums, L, M)
  root.right = self.build(nums, M + 1, R)
  
  root.sum = root.left.sum + root.right.sum
  return root
```

### update
if we want to update a node sum, we can take in the index that we want to update and the value we want to update it with. 
the implementation is similar to the `build()` function. our base case is if we reach a leaf node, we have found our 
index, and we can update the sum to the new value. then, we will calculate our `M` value. if it is smaller than the 
index, we will recursively go down the right subtree, and if it is greater than the index, we will recursively go down 
the left subtree.

this works because of the way we split our array.
```python
def update(self, index, val):
  if self.L == self.R:
    self.sum = val
    return

  M = (self.L + self.R) // 2
  
  if index <= M:
    self.left.update(index, val)
  else:
    self.right.update(index, val)
    
  self.sum = self.left.sum + self.right.sum
```
let's walk through an example:

let `i = 3` and `v = 4`, where `i` is the index for the update and `v` represents the new value we want to update. once 
we get to the base case, i.e. a leaf node, we will update the value and do it recursively.

### range query
shown below is the code for `rangeQuery` function.

```python
def rangeQuery(self, L, R):
  if L == self.L and R == self.R:
    return self.sum

  M = (self.L + self.R) // 2
  
  if L > M:
    return self.right.rangeQuery(L, R)
  elif R <= M:
    return self.left.rangeQuery(L, R)
  else:
    return self.left.rangeQuery(L, M) + self.right.rangeQuery(M + 1, R)
```
this is the most important operation of a segment tree - to calculate a range query. let's say that we are given the 
range `0,5`. from the example we have shown above, this range is in the root node, which makes it an $`O(1)`$ operation. 
of course, this is the best case scenario.

what if we are given a range that requires us to traverse down the tree? well, we will follow the same recursive procedure. 
we will recurse down the tree, and calculate the `M`. given `L` and `R`, if `L > M`, our range query lies on the right. 
if `R <= M`, our range lies on the left. and, this makes sense because when we calculated `M` in the `build()` function, 
the left subtree had indices `L, M` and right subtree has indices `M+1, R`.

in the code above, we have four conditionals. let's walk through cases under which each conditional would execute.

### time complexities
the time complexity of the three functions is as follows:

- `build()` - $`O(n)`$, where `n` is the number of nodes our tree contains.
- `update()` - $`O(log(n))`$, since we are going down the height of the tree, which is a balanced tree, where `h` is the 
height of the tree, also known as $`log(n)`$.
- `rangeQuery(L, R)` - $`O(log(n))`$, for reasons similar to the `update()` function.