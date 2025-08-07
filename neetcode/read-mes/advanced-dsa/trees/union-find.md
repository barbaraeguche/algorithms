## union find
union-find is a useful tool for keeping track of nodes connected in a graph and detecting cycles in a graph. of course, 
we can achieve this with dfs as well by using a hashset, however, this is only efficient when there is a static graph. 
if we are adding edges over time, that makes the graph dynamic, and union-find is a better choice.

### disjoint sets
union-find operates on disjoint sets. let's briefly go over them.

disjoint sets are sets that don't have any element(s) in common. formally, two disjointed sets are sets whose intersection 
is the empty set. suppose we have two sets, `S1 = {1,2,3}` and `S2 = {4,5,6}`. `S1` and `S2` are referred to as disjoint 
sets, while two sets, `S3 = {1,2,5}`, and `S4 = {5,6,7}` are not disjoint.

union-find operates on disjoint sets. if we want to perform a union of two vertices, we need to ensure that those 
vertices belong to disjoint sets.

### concept
suppose that we are given an array of edges, `edges: [1,2], [4,1], [2,4]`, which represents a graph. here, each array in 
`edges` is an undirected, connected pair of vertices, i.e. `1` is connected to `2`.

our task is to determine if this graph contains a cycle. we can solve this with union-find.

union-find is referred to as a **"forest of trees"**. initially, each vertex stands by itself, and for each vertex, 
we want to store the pointer to its parent. Since we have not connected them yet, each node is a parent to itself, 
i.e. points to itself.

next, we go through the edges to connect the vertices. we start with the first edge, `[1,2]`.

since `2` is connected to `1`, we can select it to be the child of `1`. here, it does not matter which vertex is the 
parent and which vertex is the child. however, this order starts to matter when the two components we are trying to 
union have different heights, also referred to as the rank. if you are confused about this part, don't worry, 
we will expand on this soon.

The union-find data structure has two operations. the `find` operation and the `union` operation. we want to ensure that 
we are not connecting vertices that are part of the same component. so, given a vertex, `n`, the find operation finds 
the parent of `n`. we can then use this in the union operation to join vertices together.

### implementation
to implement union-find, we can have a `UnionFind` class. within the constructor, we can instantiate our parent hashmap 
and our rank hashmap. alternatively, we can often use arrays to store the parents and ranks as well.

### the initial setup
```python
class UnionFind:
  def __init__(self, n):
    self.parent = {}
    self.rank = {}

    for i in range(1, n + 1):
      self.parent[i] = i
      self.rank[i] = 0
```

### find
our `find` function will accept a vertex `n` as an argument and return its root `parent`. we can use our parent hashmap 
where the key is the vertex and the value is the parent.

by traversing up the tree, we can find the root parent. if a vertex is a parent to itself, then it is the root parent. 

if two vertices have the same root parent, then they are already a part of the same connected component. if they have 
different parents, they are part of different connected components.

- #### path compression
as we are performing union on a large number of vertices, it can end up creating a pretty long chain, similar to a long 
linked list.

however, we can reduce the number of these steps by traversing up two vertices at a time instead of one. this would mean 
that when we are going up the tree, we can set the parent of each node to be the root parent. this process is called 
**path compression**.

we can do this recursively.
```python
def find(self, n):
  # finds the root of x
  if n != self.parent[n]:
    self.parent[n] = self.find(self.parent[n])
  return self.parent[n]
```

the line `self.parent[n] = self.find(self.parent[n])` is performing the path compression. it is updating the parent of 
the given vertex to point to the root parent.

### union
the union function takes two vertices and determines if a union can be performed.
- if the two vertices share the same root parent, a union cannot be formed and we can return false.
- if the two vertices, call them `n1` and `n2`, have parents `p1` and `p2` respectively, and `p1`'s rank is higher than 
`p2`, `p2` is the child to `p1`.
- conversely, `p1` is the child to `p2` if `p2`'s rank is higher than `p1`. 
- if the rank/height of `p1` and `p2` are equal, we can set `p2` to be the parent of `p1` and increment `p2`'s rank by 1.

```python
def union(self, n1, n2):
  p1, p2 = self.find(n1), self.find(n2)
  
  # already share a parent
  if p1 == p2:
    return False

  if self.rank[p1] < self.rank[p2]:
    self.parent[p1] = p2
  elif self.rank[p2] < self.rank[p1]:
    self.parent[p2] = p1
  else:
    self.parent[p1] = p2
    self.rank[p2] += 1
  
  return True
```

### time complexities
in the naive case, the `find` function will result in $`O(n)`$ because it is possible that the tree is just a chain like a
linked list, and we have to traverse every single node.

by implementing union by rank and path compression, we get a time complexity of $`α(n)`$, where `α` is called the
**inverse ackermann function**. it is assumed to be constant, $`O(1)`$, for nearly all input sizes.

so, if `m` is the number of edges we have, then the time complexity of union-find is $`O(m * α(n))`$ which is assumed to be
$`O(m)`$.

### space complexities
for the parent and rank hashmaps, they usually take $`0(n)`$ space, where `n` is the number of nodes.

### note:
you don't need to understand the [**inverse ackermann function**](https://en.wikipedia.org/wiki/Ackermann_function), 
just know that it is a very slow-growing function and is considered to be constant for all practical purposes.