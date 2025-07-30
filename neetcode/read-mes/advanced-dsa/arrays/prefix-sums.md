## prefix sums
a prefix sum is a super useful technique that can be used with arrays. suppose we have an array `nums = [2,-1,3,-3,4]`. 
the basic idea here is that we create an array, say, `prefix`, and fill it up such that the value at its `i`th index 
denotes the running sum of a `nums` subarray that starts from `0` and goes up to and including the `i`th index. this is
extremely useful when we want to retrieve the sum of a subarray ending at an arbitrary index, say `i`.

### time complexities
- the time complexity to build the initial prefix sum is `O(n)`. however, to calculate a range sum, we will only perform
`O(1)` operations no matter how large the array is.

### space complexities
- if we don't need the initial array, we can actually overwrite it with its prefix sum, which will bring the space 
complexity down from `O(n)` to `O(1)`. this works because the size of an array's prefix sums will be the same as the 
size of the array.