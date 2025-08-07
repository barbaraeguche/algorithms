## insertion sort
a simple sorting algorithm that builds the sorted list one element at a time, from left to right. 

it works by repeatedly taking an element from the unsorted portion and inserting it into its correct position in the 
sorted portion of the list.

it is also a stable sorting technique, i.e. the order of elements stays the same if the comparing keys are equal in value.

### time complexities
- when an array is already sorted, the time complexity: **$Ω(n)$**
- when an array is not sorted, the time complexity: **$O(n)$**

### space complexities
- sorting happens in-place: **$O(1)$**