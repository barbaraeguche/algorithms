## kruskal's minimum spanning tree (mst) algorithm
kruskal's algorithm, similar to prim's algorithm, is another algorithm for finding the minimum spanning tree in an 
undirected weighted graph. kruskal's is also a greedy algorithm that works better on sparse graphs, while prim's works 
better on denser graphs.

### the idea
kruskal's algorithm works by sorting the edges in increasing (or rather non-decreasing) order of weights; then, starting 
with an initially empty tree, considers all edges, and adds the edge with the minimum weight to our `mst`, if it does 
not result in a cycle. kruskal's will discard an edge if it results in a cycle.

### cycle detection
kruskal's makes use of the union-find data structure to detect if adding an edge would result in a cycle. recall that 
union-find data structure operates on disjoint sets. it does so by keeping track of the parent of each vertex, and if 
the two vertices we are trying to union have the same parent, it returns false since there is a cycle.

of course, at any point there will be multiple valid spanning trees, which can occur if multiple edges have the same 
weight. it does not really matter which one we pick as all of them will lead to the same cost. although, the resultant 
tree might look different.

    the visual below demonstrates the process of building the minimum spanning tree from the graph with blue edges. the 
    red edges denote that the graph is a spanning tree. the white check-marks represent valid spanning trees and the red 
    Xs represent invalid spanning trees, i.e. there is a cycle.

### implementation
we can borrow the same idea from prim's and use a `minHeap` to always get the next smallest weight. we don't need to 
build an adjacency list because we are not concerned about picking the next smallest weight of the connected components 
but rather the smallest weight of all vertices. as such, we fill our heap with `weight`, where `weight` represents the 
cost to get from `n1` to `n2`. then, we can instantiate our `UnionFind` class (we are using the code we built in our 
Union-Find chapter) where we initialize all vertices pointing to themselves. we can then repeatedly pop from our heap, 
and if we can union the popped vertices, we will append them to our `mst` list. otherwise, we will continue to the next 
element in the heap. We will continue this until `len(mst) < n - 1` since there are `n-1` edges.

```python
# given a list of edges of a connected undirected graph, with nodes numbered from 1 to n,
# return a list edges making up the minimum spanning tree.
import heapq as hq

def minimumSpanningTree(edges, n):
  minHeap = []
  for n1, n2, w in edges:
    hq.heappush(minHeap, (w, n1, n2))
  
  mst = []
  uf = UnionFind(n)
  
  while len(mst) < n - 1:
    w, n1, n2 = hq.heappop(minHeap)
    
    if uf.union(n1, n2):
      mst.append([n1, n2])
    
  return mst
```

### time complexities
the difference between kruskal's and prim's is that in kruskal's, we are using the union-find data structure. still, we
are making use of a min-heap which gives us $E$ edges to add in the worst case. io add/remove, the heap takes
$O(log(v^2))$ time, which can be reduced to $O(log(v))$, using the log power rule. this gives us a total time complexity
of $O(e * log(v))$, where $v$ is the number of vertices.

### space complexities
the memory complexity will be $O(e)$, where $e$ is the number of edges.