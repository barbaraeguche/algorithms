## graphs
a data structure made up of nodes (like list nodes and tree nodes), where the nodes may be connected by pointers. 
the number of edges, `E` given the number of vertices `V` will always be less than or equal to `V^2` *` E` <= `V^2`, 
assuming no duplicate edges are allowed.

### types of graphs
- **directed**: the pointers connecting the edges together have a direction.
- **undirected**: there are edges but no direction.

for example, trees and linked lists are directed graphs because we had pointers like `prev`, `next` and `leftChild`, 
`rightChild`.

### formats of graphs in interviews
a graph can be represented in different ways. it is an abstract concept that is made concrete using different data 
structures. most commonly, graphs are represented using the following:
- matrix
- adjacency matrix
- adjacency list

### time complexities
- adjacency list: **O(v + e)**