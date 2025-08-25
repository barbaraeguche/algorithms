## unbounded knapsack
sometimes, the question might follow a slight variation of the $0/1$ knapsack problem.

### a slight variation from 0/1 knapsack
in the previous article, we were only allowed to include each item at most once. with the unbounded knapsack, we have 
no limit on how many times we can include an item. as such, we are faced with the following question.

    Q: given a list of N items, and a backpack with a limited capacity, return the maximum total profit that can be 
    contained in the backpack. the i-th item's profit is profit[i] and its weight is weight[i]. assume you can have an 
    unlimited number of each item available.

again, we are trying to maximize our total profit by choosing items such that our capacity remains >=0. since we can 
include a given item multiple times, our decision tree's height will end up being $m$, where $m$ is the total capacity. 
this is different compared to the 0/1 where the height of our decision tree was $n$, where $n$ was the length of the 
`profit` and `weight` array.

same as before, at any given item, we can choose to include it or exclude it. the difference here is that when we 
include an item, we can **keep** on including it until we no longer have the capacity for it. here is a decision tree 
visualized. can you spot the difference?

notice that in the left subtree, we choose to include the first item twice. similarly, in the right subtree, we have 
initially chosen to exclude the first item. then, we can make a choice to include the second item or exclude it. notice 
that once we skip over an item, we cannot include it again. notice that the maximum profit we can get is $18$, where we 
choose to include $7$ twice and $4$ once. it is encouraged that you draw the rest of the decision tree yourself.

this, however, is just one way to visualize the decision tree. there is also another way to visualize this, although 
that requires looping. this would look like the visual below. for the sake of brevity, only the left subtree has been 
included, but it is enough for you to get the gist of what is going on. when `C=3`, we have the option to include 
`weight[0]` again, or `weight[1]`, `weight[2]`, `weight[3]`. the reason we are able to include `weight[0]` again is 
because we did not skip it initially, and we have an unlimited amount.

    we mentioned before that the height of this tree will be $O(2^c)/O(2^m)$ in the worst case. this makes sense because 
    if we have an item with weight of $1$ and we kept choosing that item, our decision tree would look like the 
    following.

- #### a deeper dive
to understand a little bit more about why this algorithm works, let's go into a little more detail. recall that with 
dynamic programming, it is all about breaking a problem into sub-problems. in the original problem, we have four items 
to choose from, and we could choose each item an infinite number of times. among all those possibilities, we were trying 
to maximize the profit. in the original left subtree, we were trying to include all possibilities where there was at 
least one occurrence of the first item. then, from that left subtree, if we choose to go left again, we would have 
included another occurrence of the first item. if we choose to go right, however, we would have skipped the first item 
and moved on to include the second item.

because we are only left with three items when we skip the first one, this breaks the problem down further. in the 
original right-subtree, we have all the possibilities where we include at least one second item. if we keep going to the 
right, we break the problem down even further where we choose at most one second item. notice that each time, the number 
of elements that we can choose from gets smaller, so we have fewer choices to make, until the capacity runs our and 
there are no more choices to make. this is what the tree denotes.

### implementation
- #### brute-force
implementation wise, the $0/1$ and unbounded knapsack only differ by 1 line. that is, when we choose to include item i, 
we don't need to skip item i by doing i+1 because we can include it unlimited number of times.

```python
# brute force solution
# time: O(2^m), space: O(m)
# where m is the capacity.
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
    p = profit[i] + dfsHelper(i, profit, weight, newCap)
    # compute the max
    maxProfit = max(maxProfit, p)
  
  return maxProfit
```

    it should also be noted that we are passing `newCap` instead of `capacity` in the recursive calls, which hasn't 
    changed from the previous chapter. this is because the capacity changes at every step.
even though our capacity changed, we still have access to all the elements in our `profit` and `weight` array.

- #### memoization
shown below is the memoization solution, which again differs from the same line discussed above.

```python
# memoization solution
# time: O(n * m), space: O(n * m)
# where n is the number of items & m is the capacity.
def memoization(profit, weight, capacity):
  # a 2d array, with N rows and M + 1 columns, init with -1's
  # this is our problem space - two-dimensional grid
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
    p = profit[i] + memoHelper(i, profit, weight, newCap, cache)
    # compute the max
    cache[i][capacity] = max(cache[i][capacity], p)

  return cache[i][capacity]
```

- #### bottom-up dynamic programming
the true dynamic programming approach would be the bottom-up approach. the solution to which stays the same as 0/1 
bottom-up approach, except we change one line of code, i.e. `include = profit[i] + dp[i][c - weight[i]]`. notice that it 
is very subtle - we changed `dp[i-1]` to `dp[i]`.

Because the time complexity is $O(n * m)$, the solution space is very similar, where we have an $n * m$ grid, $n$ being 
number of items and $m$ being the capacity. the bottom-right cell is going to be our answer, i.e. the last row and the 
last column. but how do we arrive at the answer for each cell? basically, we only need access to the current row and the 
previous row every time we perform a calculation. if we don't have enough capacity, we can use `dp[i-1][c]`'s value to 
fill that cell, where `dp` represents our solution space.

conversely, if we choose to include that item, we will have `include = profit[i] + dp[i][c - weight[i]]`, which will 
take the profit of the current item and add it to the value at `dp[i][c - weight[i]]`. in this case, we are not moving 
diagonally up.

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
      dp[0][c] = (c // weight[0]) * profit[0] 

  for i in range(1, N):
    for c in range(1, M + 1):
      skip = dp[i-1][c]
      
      include = 0
      if c - weight[i] >= 0:
        include = profit[i] + dp[i][c - weight[i]]
      
      dp[i][c] = max(include, skip)
  
  return dp[N-1][M]
```
and, the optimized solution for space.
```python
# memory optimized dynamic programming solution
# time: O(n * m), space: O(m)
def optimizedDp(profit, weight, capacity):
  N, M = len(profit), capacity
  dp = [0] * (M + 1)

  for i in range(N):
    curRow = [0] * (M + 1)
        
    for c in range(1, M + 1):
      skip = dp[c]
      
      include = 0
      if c - weight[i] >= 0:
        include = profit[i] + curRow[c - weight[i]]
      
      curRow[c] = max(include, skip)
    dp = curRow
  
  return dp[M]
```

this is what our solution would look like visualized, with all the values filled in the grid.

### time complexities
the time complexity of the optimized solution is $O(n * m)$ where $n$ is the number of items and $m$ is the capacity.

### space complexities
the space taken is $O(m)$ because the length of our row can only be as long as the capacity.