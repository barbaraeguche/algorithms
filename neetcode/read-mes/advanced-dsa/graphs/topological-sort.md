## topological sort
### the idea
topological sort is a way of sorting a directed acyclic graph (DAG) such that each node comes before its dependent nodes. 
a simple example of this is university courses. there are some courses that can be taken without any pre-requisites, and 
then there are those that have pre-requisites, i.e. you cannot take them unless you have taken other courses first.

in other words, some courses can be taken independent of other courses and others have to be taken in a specific order. 
we can represent this scenario using a DAG, where the edges represent the dependencies between the courses.

so, if we have node `C` and it has node `A` and `B` as its dependents, `A` and `B` will appear before `C` in the 
topological ordering. what order they appear in is not important unless `A` and `B` also have a dependency on each other.

### example
suppose we are given the following directed acyclic graph (DAG). the topological ordering for this graph would be 
`A,B,C,D,E,F`. notice that each node appears before its dependent node.

this is a rather simple example. we mentioned previously that topological sort works on acyclic graphs. what if we had 
a cycle in our graph? let's take a slight modification of the graph above and apply the same concept to it. in this 
case, we have an edge coming out of `E`, going into `A`. the order would be: `E,A,B,C,D,E,F`. this actually contradicts 
the idea of topological sort since it is not possible to have `E` before `A`, and also after `A`. this would be like 
saying to take course `A`, you must take course `E` first, but to take course `E`, you must take course `A` first - it 
is a cycle.

even if there are no cycles allowed, topological sort will still work on disconnected graphs. if we have two connected 
components in a graph, the ordering in which we place the vertices of the individual disconnected components does not 
matter as they are independent of each other. the graph below has two connected components and one possible valid 
ordering could be `A,B,C,D,E,F,G,H`.

### the algorithm
to traverse the graph, we can make use of either bfs or dfs. in our case, we will be using recursive dfs. the question 
here is what will be our base case? taking a look at our graph, it looks like we want to return when we reach `F`. 
however, this way, we will end up visiting `F` twice because `F` can be reached from `D`, but also from `E`, i.e. 
`D -> F`, `E -> F`. to avoid this, we can make use of a hashset, `visit`, to keep track of the visited nodes. this will 
result in the order `A,B,D,F,C,E,G,H`, which happens to be the wrong order. the issue here is that `F` appears before 
`C` and `E`, but `F` is dependent on both `C` and `E`.

we want to find a way so that we can visit `C` and `E` before we visit `F`. there are two common techniques that we can 
use to solve this issue.

- reverse the edges of the graph and run a post-order traversal. recall that post-order traversal is: `left, right, root`. 
this will give us the correct topological order, which is shown below.


    the numbers next to the vertices represent the order in which they are visited.

- instead of reversing the graph, perform a post-order traversal and reverse the resultant array instead. this saves us 
from reversing the graph and still gives us the correct topological order.

### topological sort without a known start point
in the examples above, we talked about graphs where we knew which vertices were the "head" of the connected components. 
however, most problems are not so convenient. still, as long as we have a list of every vertex in the input graph, we 
can solve the problem. instead of performing DFS starting from "head" (or source vertex) of each component, we will 
instead run it on every single vertex of each component in the order they appear in.

suppose the first four vertices show up in the order `B,C,H,A`. in this case, we can just perform post-order dfs one 
vertex at a time. we can visit neighbors of `B`, then neighbors of `C` and finally neighbors of `H` and `A`. by the time 
we visit the other nodes, we will have already visited them or their neighbors, so we can simply return. this would look 
like the following.

### implementation
let's assume that we are given a directed acyclic graph, and we want to return the topological order. first, we will 
build our adjacency list using our given array of edges. to store our topological ordering, we can use a list, `topSort`, 
and a `visit` hashset to avoid re-visiting the same vertex twice. we can perform our dfs and return the `topSort` list 
with the topological order.

- #### dfs
though a helper function, the `dfs` function is what builds our list. we can pass in `src`, which denotes the current 
node we are on. `adj`, which represents the adjacency list and allows us to go through the neighbors. `visit`, and 
`topSort` list, which is what we will return in the end. if the current node, `src` is already in the `visit` hashset, 
we can return. otherwise, we will add it to `visit` and perform `dfs` on its neighbors. after performing `dfs`, we can 
append the `src` to our `topSort`.

```python
# given a directed acyclical graph, return a valid topological ordering of the graph.
def topologicalSort(edges, n):
  adj = {}
  
  for i in range(1, n + 1):
    adj[i] = []
  for src, dst in edges:
    adj[src].append(dst)
  
  visit, topSort = set(), []
  
  for i in range(1, n + 1):
    dfs(i, adj, visit, topSort)
  
  topSort.reverse()
  return topSort

def dfs(src, adj, visit, topSort):
  if src in visit:
    return
  visit.add(src)

  for neighbor in adj[src]:
    dfs(neighbor, adj, visit, topSort)
  topSort.append(src)
```

- #### cyclical path
what if we were not guaranteed that the graph was acyclic? how would we go about adding some cycle detection to our 
graph? we can declare another hashset, `path`, which will keep track of the current path in our dfs. just like `visit`, 
we will add vertices to our `path`. then, once we pop from the recursion stack of a path in the graph, we will also pop 
from our `path`. if we visit the same vertex along a path twice, we can return false since this means our graph has a 
cycle.

### closing notes
in the introduction, we mentioned that one application of topological sort is course pre-requisites.

the graph below is a concrete example of this, where `A = Algebra`, `C = Chemistry`, `E = English`, and `P = Physics`. 
the topological order makes sense because you are required to take `Physics` I before taking `Physics` II, so on and so 
forth.