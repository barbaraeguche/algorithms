## two pointers
we have already seen a variation of the two pointers technique when we learned about the sliding window, which also 
involves two pointers.

the main idea is to have a `L` (left) pointer and a `R` pointer, both starting at some indices of the array. they don't 
always have to start at the beginning of the array, as is common in the sliding window technique. the `L` and `R` 
pointers can start at any index of the array.

### concept
we will start the `L pointer at `0` and `R` pointer at `arr.length - 1` and increment either the `L`, or decrement `R` 
or both depending on the conditions given in the problem. this repeats until the pointers meet each other.

### time complexities
- in both cases the time complexity is **O(n)** where `n` is the length of the input array. this is because we only 
visit each element once.