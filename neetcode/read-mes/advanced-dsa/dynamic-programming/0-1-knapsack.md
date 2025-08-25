## 0/1 knapsack
### the idea
suppose we are given a bag/knapsack with a fixed capacity, along with some items' weights and profits we reap by 
choosing to put that item in the bag. we want to maximize the profit while also ensuring that our backpack doesn't run 
out of space. the reason this algorithm is called $0/1$ is that at each point, we can either choose to include an item 
or not include it - a binary decision.

    Q: given a list of N items, and a backpack with a limited capacity, return the maximum total profit that can be 
    contained in the backpack. the i-th item's profit is profit[i] and its weight is weight[i]. assume you can only add 
    each item to the bag at most once.

your first instinct might just be to be greedy and pick the items with the most profit. however, we might not get the 
maximum profit this way because capacity might become a bottleneck, e.g. the items with the highest profits might be the 
heaviest. so, given `profit = [4,4,7,1]` and `weight = [5,2,3,1]`, we can choose to include or exclude each item. 
following the same pattern from our beginners course, we can construct a decision tree, as shown below. $C$ represents 
the capacity of our bag at any given point, the numbers in red represent the weight and the numbers in blue represent 
the total profit.

looking at the visual above, you might be able to tell that we get the highest profit when we skip the first item but 
include all the other items, i.e. which gives a total profit of 12.

    in the next article, we will go into more detail as to how the decision tree works in detail, but for now, this is 
    enough.


### implementation
when we start thinking about the code implementation, our base case will be when `i == len(profit)`. this makes sense 
because if we exhaust all items, there isn't anything to return. then, as mentioned previously, we can either skip the 
item or include the item. if we skip the item, we don't have to worry about capacity overflow or the profit.

in the case that we choose to include the item, we must calculate the new capacity **and** only include the item if 
including this item will not result in a capacity overflow. we can then calculate the profit by going down that branch 
in the decision tree, the recursive call to which will be called with the new, updated capacity each time. since we want 
to maximize our profit, we can take the maximum of two profits calculated, i.e. if our `maxProfit` was gained by 
skipping `i` or including `i`.

```python
# brute force solution
# time: O(2^n), space: O(n)
# where n is the number of items.
def dfs(profit, weight, capacity):
  return dfsHelper(0, profit, weight, capacity)

def dfsHelper(i, profit, weight, capacity):
  if i == len(profit):
    return 0

  # skip item i
  maxProfit = dfsHelper(i + 1, profit, weight, capacity)

  # include item i
  newCap = capacity - weight[i]
  if newCap >= 0:
    p = profit[i] + dfsHelper(i + 1, profit, weight, newCap)
    # compute the max
    maxProfit = max(maxProfit, p)

  return maxProfit
```

the time complexity of the code above is $2^n$. we know that $2^n$ has the potential to be really large, so there is 
bound to be some duplicate work. recall from fibonacci that we calculated `F(2)` multiple times. you might have already 
figured out that we can use memoization to optimize this!wWe can actually take this code and optimize it so that we 
bring it to $O(n ∗ m)$ complexity where $m$ is the capacity we have been given.

we can make use of a cache so that we don't have to recalculate values, we can just use the cache to retrieve them.

in the `memoization` function, `cache` represents our 2D grid where we initialize all values to `-1`. we will use this 
later to help with our base case.

```python
# memoization solution
# time: O(n * m), space: O(n * m)
# where n is the number of items & m is the capacity.
def memoization(profit, weight, capacity):
  # a 2d array, with N rows and M + 1 columns, init with -1's
  N, M = len(profit), capacity
  cache = [[-1] * (M + 1) for _ in range(N)]
  
  return memoHelper(0, profit, weight, capacity, cache)

def memoHelper(i, profit, weight, capacity, cache):
  if i == len(profit):
    return 0
  if cache[i][capacity] != -1:
    return cache[i][capacity]

  # skip item i
  cache[i][capacity] = memoHelper(i + 1, profit, weight, capacity, cache)

  # include item i
  newCap = capacity - weight[i]
  if newCap >= 0:
    p = profit[i] + memoHelper(i + 1, profit, weight, newCap, cache)
    # compute the max
    cache[i][capacity] = max(cache[i][capacity], p)

  return cache[i][capacity]
```

you might be thinking that there is not much difference between the memoization solution and the brute force approach. 
you would be correct. in the memoization solution, our input parameters are going to be `i` and `capacity`, and to 
retrieve the profit associated with an item, `items` represents our rows and `capacity` represents our columns. we can 
initially fill all of our rows as $−1$, which denotes that they have not been visited yet.

in our `memoHelper` function, we have two base cases:
- one, if our item reaches the limit of our capacity, we can return $0$. 
- if our cache already contains a value at `cache[i][capacity]`, and that value is not $−1$, we can return the value 
stored in the cache(profit has already been calculated for that position). 

if your interviewer is content with this solution, you can leave it at that. however, sometimes the interviewer may ask 
for a bottom-up solution, which may be referred to as the "true" dynamic programming solution.

### bottom-up dynamic programming approach
in this case, we are going to have 9 columns and 4 rows, representing our solution space. each row represents each item 
and each column represents the capacity available. now, assuming that all the items have a positive weight, we cannot 
include any items at in the 0th column, simply because every item's weight exceeds the capacity of $0$ - we just don't 
have enough space. again, similar to the memoization solution, we can choose to include or skip this item. if we choose 
to skip this item, its value will be the same as `i-1`st row. in other words, the value on the left.

- if we are at a row and column where the weight of the item (depicted by the row), exceeds the capacity (depicted by 
the column), we derive its value by `dp[i-1][c]`, which denotes going one row up.
- if we are at a row and column where the capacity is enough to contain the item, we derive that cell's value by taking 
the profit associated with that item, and adding it to `dp[i-1][c-weight[i]]`, which denotes going one row up, and 
`c-weight[i]` positions to the left, where `c` is the current capacity and `weight[i]` is the current item's weight. 
this denotes moving up diagonally.

in the end, we can return the value in the bottom right cell. this is what that would look like visualized.

```python
# dynamic programming solution
# time: O(n * m), space: O(n * m)
# where n is the number of items & m is the capacity.
def dp(profit, weight, capacity):
  N, M = len(profit), capacity
  dp = [[0] * (M + 1) for _ in range(N)]

  # fill the first column and row to reduce edge cases
  for i in range(N):
    dp[i][0] = 0
  for c in range(M + 1):
    if weight[0] <= c:
      dp[0][c] = profit[0]

  for i in range(1, N):
    for c in range(1, M + 1):
      skip = dp[i-1][c]
      
      include = 0
      if c - weight[i] >= 0:
        include = profit[i] + dp[i-1][c - weight[i]]
        
      dp[i][c] = max(include, skip)
  
  return dp[N-1][M]
```

### a slight memory optimization
notice in the previous solution that we are keeping an entire grid in memory the entire time. the reality is, however, 
we only need two rows in memory at a time. the current row that we are trying to fill and the row above. this is what 
the optimized solution would look like.

```python
# memory optimized dynamic programming solution
# time: O(n * m), space: O(m)
def optimizedDp(profit, weight, capacity):
  N, M = len(profit), capacity
  dp = [0] * (M + 1)

  # fill the first row to reduce edge cases
  for c in range(M + 1):
    if weight[0] <= c:
      dp[c] = profit[0]

  for i in range(1, N):
    curRow = [0] * (M + 1)
    
    for c in range(1, M + 1):
      skip = dp[c]
      
      include = 0
      if c - weight[i] >= 0:
        include = profit[i] + dp[c - weight[i]]
      
      curRow[c] = max(include, skip)
    dp = curRow
  
  return dp[M]
```

### time complexities
as mentioned before, the bottom-up approach reduces the time complexity down to $O(n * m)$ where $n$ is the number of
items and $m$ is the capacity of our knapsack. this is a big improvement from the $O(2^n)$ solution.

### space complexities
the optimized "true" dynamic programming solution has a space complexity of $O(m)$

### closing notes
dynamic programming questions can be extremely difficult at first and require lots of practice. looking at code is not 
enough, but rather, solving the problems by yourself is what makes the biggest difference.