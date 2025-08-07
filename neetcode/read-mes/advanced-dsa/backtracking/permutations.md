## permutations
we can take a **permutation** of a set of elements by creating an ordered arrangement of those elements.

for example, a permutation from the set $[1,2,3]$ could be $[1,2,3]$ or $[1,3,2]$ or $[2,1,3]$.

notice that the order of the elements is important in permutations. unlike with combinations, we want to use all the 
elements from the given set.

### generate permutations
    Q: given a distinct list of integers, return all possible distinct permutations of them.

the image below demonstrates how we can generate permutations for all numbers where the list given is `[1,2,3,4]`. we 
are given four elements, thus each permutation will be of size `4`.
- for the first element, we can choose any of the **four** elements.
- for the second element, we can choose any of the **three** remaining elements.
- for the third element, we can choose any of the **two** remaining elements.
- finally, for the last element, we can choose the **single** remaining element.

the total number of permutations we can generate is $4 * 3 * 2 * 1 = 4! = 24$. in general, the number of permutations we 
can generate is `n!` where `n` is the number of elements in the list.

we are going to implement two solutions, recursive and iterative.

### recursive solution
there are multiple ways to generate permutations. we will discuss a solution that can be implemented both recursively 
and iteratively.

let's think of how the problem can be broken down into subproblems.
- we want all permutations of $[1,2,3]$.
- we can generate permutations without including the `1`. this would be $[2,3]$ and $[3,2]$.
- to include `1` we can then insert `1` at each index of $[2,3]$ and $[3,2]$.
- the resulting permutations would be $[1,2,3]$, $[2,1,3]$, $[2,3,1]$ and $[1,3,2]$, $[3,1,2]$, $[3,2,1]$.

the above approach can be applied recursively.
- we first recursively call the `helper` function to generate all permutations without including the element at index `i`.
- we then use nested loops to insert the element at index `i` in to each position in each permutation that was generated.

```python
# time: O(n^2 * n!)
def permutationsRecursive(nums):
  return helper(0, nums)

def helper(i, nums):
  if i == len(nums):
    return [[]]

  resPerms = []
  perms = helper(i + 1, nums)
  
  for p in perms:
    for j in range(len(p) + 1):
      pCopy = p.copy()
      pCopy.insert(j, nums[i])
      resPerms.append(pCopy)
      
  return resPerms
```

### iterative solution
in the iterative solution, instead of performing the recursive call, we will just loop through nums, `for n in nums`. 
toward the end of each `perms` loop, we can update our `perms` to be `nextPerms` so that we are not creating the same 
copy at each iteration.

```python
# time: O(n^2 * n!)
def permutationsIterative(nums):
  perms = [[]]

  for n in nums:
    nextPerms = []
    
    for p in perms:
      for i in range(len(p) + 1):
        pCopy = p.copy()
        pCopy.insert(i, n)
        nextPerms.append(pCopy)
        
    perms = nextPerms
  return perms
```

### time + space complexities
if the number of elements we are provided is `n`, then at each element, we have `n!` permutations. however, inside each 
for loop, in both the solutions, we have another for loop that runs from `0` to each permutation's length, which is `n`
because we are using all the elements. as a result, we get $n^2 * n!$, which results in $O(n^2 * n!)$.