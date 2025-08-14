## prim's minimum spanning tree (mst) algorithm
prim's algorithm is used to find a spanning tree with the minimum cost. similar to dijkstra, prim's is also a greedy 
algorithm and works on weighted undirected graphs.

but what is a spanning tree? if we are given a graph $G$, a spanning tree is a subset of edges from $G$ where the total
weight of the edges is minimized. so, it is similar to dijkstra in the sense of minimizing the cost.

recall that by definition, a tree is a connected graph, the same is true for a minimum spanning tree. however, a tree 
cannot have any cycles. this means that if $G$ has $n$ nodes, our minimum spanning tree will have at most $n−1$ edges.

### the idea
$G$ could have multiple valid minimum spanning trees with the same cost. So, given $G$, how do we go about finding the 
minimum spanning tree? we will start with an empty spanning tree, and at each vertex, we pick the connected vertex with 
the smallest weight, among all of its neighboring vertices. when we reach $n−1$ edges, we can stop our algorithm. in the 
visual below, for the mst, we start at vertex `A`, where the minimum cost of the connected component is $1$ `A -> B`, 
after which we have $2$ `B -> C`, which gives us $n−1$ edges and a minimum cost of $3$. the spanning tree at the bottom 
of the visual is another valid spanning tree, but it is not a minimum cost spanning tree.

    one application of the minimum spanning tree is a road network among cities. using the example above, if we wanted 
    to connect city `A`, `B` and `C` together, it can be done so using the concept of a mst.

### the algorithm
suppose we are asked to find the minimum spanning tree for a graph. similar to dijkstra, finding the next connected 
component with the minimum cost can be done using a min-heap. each heap node will have `<weight, n1, n2>`, where `weight` 
represents the cost from `n1` to `n2` vertices. to avoid cycles, and keep track of the number of nodes, we can use a 
hashset named `visit`. we will then build our `mst` from scratch, adding one edge at a time. there are three different 
conditions we can use to terminate the execution of the algorithm:
- keep popping from the min-heap until it becomes empty
- stop once `visit.size() == n`, i.e. we have visited all the nodes
- keep track of the number of edges in our mst. When our edges reach $n−1$, we can stop the algorithm

    
    in the visual below, we build one of the valid mst from scratch given the graph shown in blue edges. notice that in 
    this implementation, we stop the algorithm once we have our valid mst, regardless of the state of our min-heap.

- #### code implementation
if we are given an array of `edges`, we will have to build an adjacency list. since our graph is undirected, we must 
append our source to the destination and our destination to the source. `adj` is a hashmap where the key is every vertex 
in the graph, and it maps to a list of its respective neighboring vertices and their respective weights.

in our `minHeap`, we will push the weight (key of our minheap), the source and the neighbor of that source. we can use
a list `mst`, which will keep track of all the edges in our spanning tree. `set()`, which allows us to keep track of the
visited nodes. then, while our `visit < n`, we will pop from our heap, which gives us the `w`, `n1` (source) and `n2`
(neighbor of `n1`) and if we have already visited `n2`, we can skip it and continue to the next element in the heap.
otherwise, we will add `n1` and `n2` to our `mst` and mark `n2` as visited. we will then visit the neighbors of `n2`
and push to our `minHeap`. once `len(visit) == n`, we will have all the edges for a mst and can return `mst`.

```python
import heapq as hq

# given a list of edges of a connected undirected graph, with nodes numbered from 1 to n,
# return a list edges making up the minimum spanning tree.
def minimumSpanningTree(edges, n):
  adj = {}
  
  for i in range(1, n + 1):
    adj[i] = []
  
  for n1, n2, w in edges:
    adj[n1].append((n2, w))
    adj[n2].append((n1, w))

  # initialize the heap by choosing a single node
  # (in this case 1) and pushing all its neighbors.
  minHeap = []
  for u, w in adj[1]:
    hq.heappush(minHeap, [w, 1, u])

  mst, visit = [], {1}
  
  while len(visit) < n:
    w, n1, n2 = hq.heappop(minHeap)
    if n2 in visit:
      continue

    mst.append([n1, n2])
    visit.add(n2)
    
    for v, w in adj[n2]:
      if v not in visit:
        hq.heappush(minHeap, [w, n2, v])
        
  return mst
```

### time complexities
since the algorithm is so similar to dijkstra's algorithm, the time complexity will be the same - $O(e * log(v))$, where
$e$ is the number of edges and $v$ is the number of vertices.

### space complexities
the space complexity is $O(e)$ since our hashset grows linearly to the number of edges our graph has.

### closing notes
prim's algorithm does not work on disconnected graphs because there is no way to create a spanning tree with a 
disconnected graph. even if there are two components within a disconnected graph, we can only find the spanning tree for
each individual component.