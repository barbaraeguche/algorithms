## merge sort
a divide-and-conquer algorithm for sorting an array or list of elements. 

it works by recursively dividing the unsorted list into ***n*** sub-lists, each containing one element. then, it repeatedly 
merges sub-lists to produce new sorted sub-lists until there is only one sub-list remaining.

it is also a stable sorting technique, i.e. the order of elements stays the same if the comparing keys are equal in value.

### time complexities
- we have ***$log(n)$*** levels, and ***n*** cost at each level: **$O(n * log(n))$**

### space complexities
- we allocate a temporary array in the ***mergeArray*** function: **$O(n)$**