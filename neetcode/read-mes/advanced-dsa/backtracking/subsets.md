## subsets
combinatorics is a branch of discrete mathematics that concerns itself with permutations, subsets and combinations. as
a matter of fact, graphs, which we have discussed before, are also a branch of combinatorics.

### concept of a subset
formally, in mathematics, if we have two sets, `Set A` and `Set B`, `Set A` is a subset to `Set B` if all of its elements 
are found in `Set B`.

additionally, any set is a subset of itself and an empty set is a subset of every set. order is not important in subsets, 
but the elements within a set must be distinct.

for example, suppose we are given `Set A = {1,2,3,4,5}` and `Set B = {5,2,1}`. `Set B` is a subset of `Set A` because it 
only contains elements that can be found in `Set A`.

changing the order of `Set B` to `{2,5,1}` does not change the set itself, so it is still a subset of `Set A`.

given `Set C = {9,10,11,12}` and `Set D = {6, 9, 10}`, `Set D` is not a subset of `Set C` because it contains a `6`, 
which `Set C` does not have.

### subsets - distinct elements
    Q: given a list of distinct nums, return all possible distinct subsets.

recall from backtracking that once we make a choice to go down a path, we backtrack and explore other choices. applying 
this concept to subsets would mean that for each element, we explore all the subsets that include that element. we then 
backtrack to explore all the subsets that don't include that element. we do this until we exhaust all the elements and 
by the end, we will have ended up with all possible distinct subsets.

in the implementation, we have two functions: `subsetsWithoutDuplicates` and `helper`.

- `subsetsWithoutDuplicates`

if the list we have been given does not contain duplicates, we will implement the function `subsetsWithoutDuplicates`. 
in this method, we will declare a list of lists `subsets` and another list `currSet`. once we build each `currSet`, we 
will add it to `subsets`.

to build each `currSet`, we will need a `helper` method.

```python
def subsetsWithoutDuplicates(nums):
  subsets, curSet = [], []
  
  helper(0, nums, curSet, subsets)
  return subsets
```

- `helper`

we will pass in an initial index `i`, `nums`, which is our list, `currSet` and `subsets` to the `helper` function. we 
will then iterate through the entire list, append the current number in nums and apply our standard backtracking 
algorithm, i.e. recurse until we hit the base case and then `pop` from `currSet` so that we can go down the path where 
we decide to not include the current element.

```python
def helper(i, nums, curSet, subsets):
  if i == len(nums):
    subsets.append(curSet.copy())
    return

  # decision to include nums[i]
  curSet.append(nums[i])
  helper(i + 1, nums, curSet, subsets)

  # decision NOT to include nums[i]
  curSet.pop()
  helper(i + 1, nums, curSet, subsets)
```

### subsets - non-distinct elements
    Q: given a list of nums that are not necessarily distinct, return all possible distinct subsets.

in this problem, we are given a `nums` that contain duplicates. to create concrete subsets, we first sort the array so 
all duplicates are adjacent to one another. we can then run a while loop to skip over the duplicates. this is different 
from the previous problem because in this case, when we backtrack, i.e. pop from the `curSet`, we run a while loop to 
skip over the duplicates before calling `helper2` again. We also make sure that our `i` pointer does not go out of bounds.

this is the difference between `helper` and `helper2`.

```python
def subsetsWithDuplicates(nums):
  nums.sort()
  subsets, curSet = [], []
    
  helper2(0, nums, curSet, subsets)
  return subsets

def helper2(i, nums, curSet, subsets):
  if i == len(nums):
    subsets.append(curSet.copy())
    return

  # decision to include nums[i]
  curSet.append(nums[i])
  helper2(i + 1, nums, curSet, subsets)
  curSet.pop()

  # decision NOT to include nums[i]
  while i + 1 < len(nums) and nums[i] == nums[i + 1]:
    i += 1
    
  helper2(i + 1, nums, curSet, subsets)
```

### time complexities
we build a recursive decision tree to explore all possible subsets. for every decision we can make, we can either include 
or not include the current element. this results in a branching factor of `2` and a height of `n`.

thus, there are roughly $`2^n`$ possible subsets. for each subset, we create a copy of it before adding it to the final 
list of subsets. the max length of a subset could be proportional to the length of the input list `nums` which is `n`.

thus, the overall time complexity is $`O(n * 2^n)`$.

### space complexities
if we are not including the space needed to store the final list of subsets, the space complexity is $`O(n)`$.

this is because we are using recursion and the space needed to store the current subset is proportional to the length of 
the input list `nums`.