## binary trees
a type of data structure in which the left and/or right pointers refer to the preceding or following tree nodes, respectively.

### binary search trees
a kind of binary tree where the value of a left child is ***less than*** its parent value, and that of a right child is 
***greater than*** its parent value.

### to note:
- the height/depth of every node is 1

### time complexities
- search: **O(log(n))** given that it is roughly balanced, else **O(h)**
- insertion/deletion: **O(log(n))** given that it is roughly balanced, else **O(h)**

~ where **h** is the height of the tree