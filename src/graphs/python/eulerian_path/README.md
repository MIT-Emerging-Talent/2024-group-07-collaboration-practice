# The Eulerian Path problem 

Given a graph, is it possible to traverse every edge exactly once, starting and ending at any vertex?

## Contents

- [Introduction]
- [Implementation]
- [Behavior]
- [Test Cases]
- [Running Tests]

## Introduction

For a graph to have an Eulerian path, it must satisfy the following: 

a- Connectedness: The graph must be connected. In the context of Eulerian circuits, it is also required that every vertex has even degree (an even number of edges connected to it).

b- Eulerian Path: If there are exactly two vertices (nodes) with an odd degree in the graph, an Eulerian path is possible, and those two vertices (nodes) will be the start and end points of the path. If there are no vertices (nodes) with an odd degree, an Eulerian circuit is possible.

## Implementation

The first step in the implementation is pick the algorithm, in the case here, Fleury's algorithm, generally this problem can sovled as follows, be a ware that the implementation follows the solution: 

1 - First we check the connectedness of the graph, a graph is considered connnected if there is a path between each pair of nodes, if the graph is not connected then there will not an Eulerian Path. 
2- Degrees of the nodes of the graph, it is a number that represents the number of edges that are connected to a given node for a graph is there are two exactly twp vertices (nodes) with odd degrees, then and Euler path is possible.  
3 - Finally if our graph passes the tests above we can construct an Eulerian graph. 
4- Un important concept emerges here, which the concept of the "bridge", and edge is considered a bridge if by removing it, the graph becomes disconneted, i.e. it is same idea as the idea of a bridge in a city, so in our implementation, we want to be sure that removeing an edge will not affect the graph. 
5 - To implement Fleury's algorithm here, we utalize the DFS algorithm, we use this function to check the connectivity of the graph as well as checking for bridges. 
6 - The graphs are represented by the adjacency list, here a dictionary is utlized where, the keys represent the nodes and values are list of the nodes that are connected to that node 

## Behavior

1- Two helper functions are written to check connectivity of the graph, a starting point is chosen, then iterate through the graph until no edge is left, in each iteration select an edge that does not disconnect the graph, remove it from the graph.
2 - The selected edges form the Eulerian path.  

## Test Cases
### Test 1: Eulerian Path Exists
- This test checks scenarios where an Eulerian path should exist in the graph.
- **Test Cases:**
  1. A graph with vertices `[0, 1, 2, 3]` where each vertex has degree 3.
  2. A graph with vertices `[0, 1, 2, 3, 4]` where vertices 1 and 2 have degree 2, and the rest have degree 3.

### Test 2: No Eulerian Path Exists
- This test checks scenarios where no Eulerian path exists in the graph.
- **Test Cases:**
  1. A complete graph with vertices `[0, 1, 2]` where each vertex has degree 2.
  2. A graph with vertices `[0, 1, 2, 3, 4]` where vertices 3 and 4 are connected to form an isolated component.

## Running tests
- to run the tests execute python test_eulerian_path.py 