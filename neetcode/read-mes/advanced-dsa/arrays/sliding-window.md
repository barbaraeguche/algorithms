## sliding window

### sliding window (fixed size)
the idea behind having a fixed sliding window is to **maintain** two pointers that are **_k_** apart from each other 
and fit a certain constraint.

the idea is the same as what we discussed in the previous chapter when we introduced the sliding window variation of 
kadane's algorithm. in this case, we must maintain a window of size `k` and within our window.

hash sets allow us to store unique elements and have an `O(1)` lookup, removal and add complexity. if we needed more 
than just two occurrences, we could use a hash map to store the count of each element, but in this case a set is 
sufficient.

we can use a set to store elements currently in our window. when our set's size goes beyond `k`, we can remove elements 
shift the left pointer and remove the element that is no longer in our window.

since we are adding from the right, if we encounter a number that has already been added, we can return true. our set's 
size should never exceed `k`.

### sliding window (variable size)
another variation of the sliding window technique is the variable size sliding window. this is useful when we don't 
have a fixed window size, and we need to keep expanding our window as long as our window meets a certain constraint.


### time complexities
- fixed: we bring the time complexity down from **O(n^2)** to **O(n)** because we only perform a single pass on the 
array and our hashset allows us to have **O(1)** lookup.
- variable: **O(n)**

### space complexities
- fixed: the space complexity is **O(k)** because we are storing at most `k` distinct elements in our hashset.