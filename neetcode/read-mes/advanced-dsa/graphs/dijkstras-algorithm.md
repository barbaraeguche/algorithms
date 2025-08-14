## dijkstra's algorithm
having already covered bfs, we will now cover another shortest path algorithm - dijkstra's algorithm. the downside of 
using bfs is that it only works when the graph is unweighted - i.e. where the default weight of each edge is 1.

if we are given the following unweighted graph: `edges = [[A,B], [A,C], [B,D], [C,B], [C,D], [C,E], [D,E]]`, and are 
asked to find the shortest path from `A` (source node) to `D` (destination node), we can apply classic bfs and keep 
adding the weights until we get to `D`.

because all the weights are the same, bfs gives the shortest path in terms of the amount of vertices we visit. however, 
this fails when we have different weights for different edges as shown below.

dijkstra's algorithm is used to find the shortest path to all nodes in a weighted graph. it is similar to bfs, except it 
operates on weighted graphs. because dijkstra's algorithm operates on different weights, it will prioritize finding the
shortest path such that the path to each destination is the "lightest".

in other words, bfs does not revisit nodes but dijkstra will, if it finds a shorter path (in terms of weight).

### the setup
suppose we are faced with the following question:

    Q: starting from A, find the length of the shortest path to every other node.

given the previous weighted graph, and a source vertex, `A`, we want to find the shortest paths from `A` to every other 
vertex in our graph. it should be noted that when we say "shortest", it means "lightest", i.e. paths that have the 
smallest total weight (the sum of the weight for the edges on the path).

starting from `A`, the shortest path to reach `C` is `A -> C`, with a weight of `3`. and, this is guaranteed to be the 
shortest path. this makes sense because `A -> B` costs `10`, so even if there was a path to `C` through `B`, it would 
never be less than `4`. this only works if we have no negative weights. the visual below demonstrates the graph, 
`edges = [[A,B,10], [A,C,3], [B,D,2], [C,B,4], [C,D,8], [C,E,2], [D,E,5]]`, and the numbers under the letters denote 
the shortest path to that vertex.

- #### walk-through of dijsktra's algorithm
let's go over how we came to the above result. since `A` is the source vertex, and no self-loop, distance from `A` to
`A` is $0$. from `A`, we can take `A -> B` (10) and `A -> C` (3). from `B` and `C`, we can take `B -> D` (2), 
`C -> B` (4), `C -> E` (2), `C -> D` (8).

- for `B`, we can update our shortest path to $7$ since `B` can be reached through `C` $3 + 4 = 7 < 10$.
- the only way to reach `C` is `A -> C`, so the shortest path to `C` is $3$.
- `D` can be reached through `A -> B`, `A -> C -> B` or `A -> C`. the shortest path is `A -> C -> B -> D`, i.e. 
$3 + 4 + 2 = 9$.
- `E`'s shortest path is `A -> C -> E`, i.e. $3 + 2 = 5$. other valid paths to `E` are `A -> B -> D -> E`, 
- `A -> C -> D -> E`, and `A -> B -> D -> E`.


    dijkstra's algorithm is a classic example of a greedy algorithm. a greedy algorithm makes the optimal choice at each 
    step, meaning it selects the best option available at each step. in this case, the smallest weight.

### implementation
since we are choosing the path with the minimum weight, a min-heap is the perfect data structure here. each "node" in 
the min-heap will contain the node letter and the cost associated with that node, like `<cost, node>`.

    notice that cost is the first element in the tuple. this is because we want to sort the min-heap by the cost.

since we are optimizing for the shortest path, it might be the case that we have to add the same vertex many times to 
get the shortest possible path. we will also declare a hashmap to map our vertices and their respective shortest paths.

    the visual below demonstrates the step-by-step process of how the min-heap implementation works to find the shortest 
    path. we always pop the node with the lowest cost.

the code implementation of dijkstra is rather simple. firstly, given a pair of `edges`, we want to build an adjacency 
list so that we can traverse the graph. `adj` represents this adjacency list. we will initialize our list with the 
source `s` vertex, `d` (destination) and `w` (weight). this part connects all the vertices together with their weights.

we then use another hashmap `shortest`, which contains our vertices and their respective shortest paths. this is what 
we will return. we will then add our `src` to our `minHeap` and its weight, `0`. we will then run a while loop until our
`minHeap` is empty. because it is a min-heap, we will always be popping the edge with the smallest weight. if we have 
already visited a vertex, i.e. it has been popped before, we will skip this vertex. otherwise, we will visit all the 
neighbors of the popped vertex, and if the neighbor is unvisited, we add it to our `minHeap`, with its respective weight. 
in this particular implementation, `shortest` will only return once we have exhausted the `minHeap`, even if it requires 
skipping the vertices.

```python
import heapq as hq

# given a connected graph represented by a list of edges, where edge[0] = src, edge[1] = dst, and edge[2] = weight.
# find the shortest path from src to every other node in the graph. there are n nodes in the graph.
# O(e * log(v)), O(e * log(e)) is also correct.
def shortestPath(edges, n, src):
  adj = {}
  
  for i in range(1, n + 1):
    adj[i] = []
  
  # s = src, d = dst, w = weight
  for s, d, w in edges:
    adj[s].append((w, d))

  shortest, minHeap = {}, [(0, src)]
  
  while minHeap:
    w1, n1 = hq.heappop(minHeap)

    # found a previous shorter path
    if n1 in shortest:
      continue
    shortest[n1] = w1
    
    for w2, n2 in adj[n1]:
      if n2 not in shortest:
        hq.heappush(minHeap, (w1 + w2, n2))
  
  return shortest
```

### time complexities
the time complexity of this algorithm can be written as $O(e * log(e))$, where `e` is the number of edges. recall that 
in the worst case, each vertex is connected to the other, i.e. $v^2$. in the worst case, we might have every single edge 
inside our heap. since insertion and removal from a heap is $log(n)$, this gives us a total of $O(e * log(e))$.

### closing notes
you might have noticed that the graph we were operating on does not contain any negative weights. this is actually one 
of the weaknesses of dijkstra. it cannot handle negative weights. this makes sense because in the graph above, we 
assumed that there couldn't exist a path to `C` through `A -> B` because `A -> C = 3` and `A -> B = 10`. knowing that 
`A -> B` is "heavier" than `A -> C`, a shorter path to `C`, through `B` is not possible under dijkstra. however, what 
if we have a negative weight such that we could find a path to `C` even shorter than $3$? for this, there is another 
algorithm - **bellman-ford shortest path algorithm**. we will not cover this algorithm in our course, but here is a 
[neetcode yt video](https://www.youtube.com/watch?v=5eIK3zUdYmE) that explains it, if that is something that interests 
you.