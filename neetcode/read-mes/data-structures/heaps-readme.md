## heaps 
a specialized, tree-based data structure. it implements an abstract data type called the priority queue, but sometimes 
'heap' and 'priority queue' are used interchangeably.

### types of heaps
- **min heaps**: have the smallest value at the root node. the smallest value has the highest priority to be removed.
- **max heaps**: have the largest value at the root node. the largest value has the highest priority to be removed.

### heap properties
for a binary tree to qualify as a heap, it must satisfy the following properties:

- **structure property**: a binary heap is a binary tree that is a complete binary tree, where every single level of 
the tree is filled completely, except possibly the lowest level nodes, which are filled contiguously from left to right.
- **order property**: the order property for a min-heap is that all the descendents should be greater than their 
ancestors. in other words, if we have a root with value `y`, every node in the right and the left subtree should have 
values greater than or equal to `y`. this is a recursive property, similar to binary search trees.

### one-based indexing
the reason why we start filling up our array from index `1` is because it helps us figure out the index at which a node's 
left child, right child, or the parent resides. because binary heaps are complete binary trees, no space is required for
pointers. instead, a node's left child, right child and parent can be calculated using the following formulas, where
*i* is the index of a given node.
- `parent` = *i* // 2
- `leftChild` = 2 * *i*
- `rightChild` = 2 * *i* + 1

### time complexities
- top(min/max): **$O(1)$**
- push/pop: **$O(log(n))$**
- heapify: **$O(n)$**