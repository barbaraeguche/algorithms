## quick sort
a divide-and-conquer sorting algorithm that works by partitioning an array into two smaller subarrays based on a 
pivot element. 

the elements less than the pivot go to the left subarray, and those greater go to the right subarray. the algorithm 
then recursively sorts the subarrays.

it is not a stable sorting technique, i.e. the order of elements do not stay the same if the comparing keys are equal 
in value. e.g. for an array [7,3,7,4,5], if the pivot is 5, after looping through all the elements, the array would 
look like this: [3,4,7,7,5]

### time complexities
- in the best case, we pick a pivot such that we can always perform the partition in the middle: **$O(n * log(n))$**
- in the worst case, the pivot is either the smallest or largest element: **$O(n^2)$**

### space complexities
- sorting happens in-place: **$O(1)$**