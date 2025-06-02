## binary search
a search algorithm where we discard a certain side of an array if the sought value cannot be found in that 
section. 

we do this by finding the midpoint of a certain range then determine what part to discard. e.g. in the array [1,3,5,7,9], 
let's say we're searching for number 9; the mid-value here is 5, so we can discard the range before 5 and continue our
search on the right-hand side of 5.

### time complexities
- always: **O(log(n))**