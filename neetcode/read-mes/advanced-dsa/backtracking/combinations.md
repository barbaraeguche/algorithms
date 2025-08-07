## combinations
### the concept
combinations are very similar to subsets in that we are choosing elements from a set. the order the elements are placed 
in also does not matter.

generally, the main difference is that a combination is a subset of a specific size `k`, where `k` is a number that is 
less than or equal to the size of the original set.

### example using combinations
    Q: Given two integers `n` and `k`, return all possible combinations of size = k, choosing from values between `1`
    and `n`.

suppose `n=5` and `k=2`. the question is asking, "how many ways are there to choose unique subsets of size `2` from a 
set of numbers that look like $[1,2,3,4,5]$".

the constraint here is that our combinations can only be of size `2`. recall that changing the order of elements does 
not result in a new combination, i.e. `[2,1]` and `[1,2]` only count as 1 unique combination.

for the given example, there are 10 combinations of size `2` as follows: $[1,2]$, $[1,3]$, $[1,4]$, $[1,5]$, $2,3]$,
$[2,4]$, $[2,5]$, $[3,4]$, $[3,5]$, $[4,5]$

so, how do we go about solving this? there are two approaches.

- #### trivial approach
this approach is similar to that of the subsets. We iterate through `1−5` in our decision tree and make a decision to 
include or exclude the current number we are on.

we are also restricted by the number of elements we can include in our combination. since `k=2`, our base case hits when 
`curComb.length == k`. this is why when we reach `[1,2]`, we don't need to go any farther.

```python
# given n numbers (1 - n), return all possible combinations of size k. (n choose k math problem).
# time: O(k * 2^n)
def combinations(n, k):
  combs = []
    
  helper(1, [], combs, n, k)
  return combs

def helper(i, curComb, combs, n, k):
  if len(curComb) == k:
    combs.append(curComb.copy())
    return
  if i > n:
    return

  # decision to include i
  curComb.append(i)
  helper(i + 1, curComb, combs, n, k)
  curComb.pop()

  # decision to NOT include i
  helper(i + 1, curComb, combs, n, k)
```

this approach will result in a decision tree with a branching factor of `2` and a height of `n`. we will also need to 
create a deep copy of each generate combination, which will be of size `k`.

thus, the overall time complexity is `O(k * 2^n)`.

you might notice that the above code is very similar to the subsets lesson with some small differences:
- in our `helper` function, `i` denotes the current number (from `1` to `n`) we are on.
- `currComb` represents the current combination.
- `combs` represents the list of lists which will contain each `currComb`.
- `k` represents the size of the target combination.
- our base case hits when the length of the `currComb` hits `k`. after exploring combinations including each `i`, we 
backtrack and explore other combinations that exclude `i`. we repeat this until `i == n`.

- #### optimized approach
in the beginning of this chapter, we mentioned that there is a neat mathematical formula to find the number of 
combinations. the formula is more efficient than $`k * 2^n`$ and is as follows: $$\frac{n!}{k!(n - k)!}$$

also known as $$\binom{n}{k}$$ (pronounced `n` choose `k`). this notation reads, "how many ways are there to choose `k` 
objects from a set of `n` elements?" or `N choose K`.

in the previous solution, there are a lot of wasted steps where we are skipping elements, and this results in a decision 
tree that is of size $2^n$.

we can use a more optimized approach that is $O(k * C(n,k))$ where $C(n,k)$ is the number of combinations we need to 
generate.

instead of choose which elements to include or exclude, we can simply choose which elements to include.

for the first element, we can choose from `1` to `n`.

for the next element, we can choose any except for the one we just chose.

the easiest way to keep track of this and also eliminate duplicate solutions at the same time is to do this: only choose 
elements in ascending order.
- choose from `1` to `n`.
- choose from `x + 1` to `n` where `x` is the element we chose in step 1.

this way each combination is always generated in sorted order, which is useful because it means if we generate `[1,2]` 
we will never generate the duplicate `[2,1]`.

given `n=5` and `k=2`, we get: 
$$
\frac{5!}{2! * (5 - 2)!} = \frac{5!}{2! * 3!} = 10
$$

```python
# time: O(k * C(n, k))
def combinations2(n, k):
  combs = []
  
  helper2(1, [], combs, n, k)
  return combs

def helper2(i, curComb, combs, n, k):
  if len(curComb) == k:
    combs.append(curComb.copy())
    return
  if i > n:
    return

  for j in range(i, n + 1):
    curComb.append(j)
    helper2(j + 1, curComb, combs, n, k)
    curComb.pop()
```