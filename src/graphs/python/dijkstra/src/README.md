# Introduction 
- Dijkstra's algorithm is a method for finding the shortest paths between nodes in a weighted graph.

- A path is a sequence of vertices that are connected by edges or in another words, 
  it's a route that starts from one vertex (the source or starting point) and reaches another vertex (the destination or endpoint) by traversing edges.

- A weighted graph is a type of graph in which each edge has an associated numerical value called a "weight.", in our case here
 The weights represent some measure of distance. 

# How the alogorithm works?

1. Start:Begin at a selected "start" vertex.

2. Explore:Visit neighboring vertices and calculate the distance from the start.

3. Update: If a shorter path is found to a vertex, update its distance.

4. Move:Move to the unvisited vertex with the shortest distance.

5. Repeat:Continue exploring and updating until all vertices are visited.

6. Result: The final distances show the shortest paths from the start vertex to all others.

# Implementation
- Since the algorithm calculates distances and stores them, here data storage structure is created for this. 
-   

 