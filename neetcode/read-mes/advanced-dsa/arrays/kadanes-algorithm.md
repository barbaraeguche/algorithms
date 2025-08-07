## kadane's algorithm
a greedy/dynamic programming algorithm that can be used on an array. it is used to calculate the maximum sum subarray 
ending at a particular position and typically runs in $`O(n)`$ time.

### optimizing with kadane's algorithm
kadane's algorithm tells us that there is a way to calculate the largest sum by only making one pass on the array, 
bringing the complexity down to linear time. let's look at how that can be done.

since we are looking for the largest sum, it is a good idea to avoid negative numbers because we know that contradicts 
what the question is asking for. negative numbers will only make our sum smaller.

but sometimes we may need to include a negative number to get the surrounding positive numbers.

- for example, the array `[6, -2, 7]` has a maximum sum of `11`. if we exclude the `-2`, we can't include both `6` and `7`.
- but that's not always the case. if we have `[1, -3, 7]`, the maximum sum is `7`. including the `-3` isn't worth it just 
to get the `1`.

the pattern is that if we ever have a negative subarray sum, we should discard it and start a new subarray. 
this is because we know that the sum will only get smaller if we include it.

- kadane's algorithm runs one loop. 
- we keep track of the `curSum` by adding the current element to it. 
- before we add the current element, we check if the `curSum` is negative. if it is, we reset it to zero. 
- we initialize the `maxSum` to the first element in the array. this is technically a subarray of size 1. (we could have 
initialized it to any other element in the array.)
- we update the `maxSum` by taking the maximum of the current sum and the maximum sum so far.

it's possible that every element in the array is negative. in that case, the maximum sum would be the largest negative
number.