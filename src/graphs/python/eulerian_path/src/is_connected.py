def is_connected(graph, u, v):
    '''
      Check connectivity using Depth-First Search (DFS)
      par:
      graph: a graph representd by the adjacency list
      u, v = nodes on the graph
      '''
    # pick a starting node, check for its degree first, if greater than one, then its a good start
    # the logic behind this is that, if it is a node has a higher degree, then it is likely the DFS
    # will cover more of the graph fast. 
    start_node = u if len(graph[u]) > 1 else v
    # store the visited nodes in a set, a set is efficient because it discards duplicates 
    visited = set()
    # The DFS function takes a par. node and explores its neighbours rescursivley, 
    def dfs(node):
        # the current node to visited nodes
        visited.add(node)
        # explore the neighbors of the  node 
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    #initiate the  dfs search inside the is_connected function
    dfs(start_node)
    return len(visited) == len(graph)

''' the is bridge function check if an edge is a bridge
par:
u,v : nodes
- graph_copy: takes a copy of the graph represented using the adjacency list
- the function removes and edge then checks if the graph is connected, then it return
the edge back and check another edge, 
- return True if removing an edge makes the graph disconnected meanning that there is an edge. 
'''
def is_bridge(u, v, graph_copy):
    # Temporarily remove the edge (u, v) and check connectivity
    graph_copy[u].remove(v)
    graph_copy[v].remove(u)
    connected = is_connected(graph_copy, u, v)  # Use DFS for connectivity check
    # Restore the removed edge
    graph_copy[u].append(v)
    graph_copy[v].append(u)
    return not connected
