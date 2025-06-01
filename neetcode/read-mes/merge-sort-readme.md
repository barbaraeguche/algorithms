## merge sort
a divide-and-conquer sorting technique in which an array is recursively divided into smaller halves, then merged in sorted order.

it is also a stable sort, i.e. the order of elements stays the same if the comparing keys are equal in value.

### time complexities
- we have ***log(n)*** levels, and ***n*** cost at each level: **O(n * log(n))**

### space complexities
- we allocate a temporary array in the ***mergeArray*** function: **O(n)**