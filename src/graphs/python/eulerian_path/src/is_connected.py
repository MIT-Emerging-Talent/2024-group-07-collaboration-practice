def is_connected(graph, u, v):
    '''
    Check connectivity using Depth-First Search (DFS)
    Args:
        graph: a graph represented by the adjacency list
        u, v: nodes on the graph
    '''
    # Pick a starting node; check for its degree first.
    # If greater than one, it's a good start.
    # The logic is that a node with a higher degree is likely to cover more of the graph quickly in DFS.
    if len(graph[u]) > 1:
        start_node = u
    else:
        start_node = v

    # Store the visited nodes in a set; a set discards duplicates efficiently.
    visited = set()

    # The DFS function takes a par. node and explores its neighbours recursively.
    def dfs(node):
        # Add the current node to visited nodes.
        visited.add(node)
        # Explore the neighbors of the node.
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    # Initiate the DFS search inside the is_connected function.
    dfs(start_node)
    return len(visited) == len(graph)

def is_bridge(u, v, graph):
    '''
    Check if an edge is a bridge.
    Args:
        u, v: nodes
        graph: graph represented using the adjacency list
    Returns:
        True if removing an edge makes the graph disconnected, meaning that it is a bridge.
    '''
    # Create a copy of the graph to avoid modifying the original graph.
    graph_copy = {node: neighbors[:] for node, neighbors in graph.items()}

    # Temporarily remove the edge (u, v) and check connectivity.
    graph_copy[u].remove(v)
    graph_copy[v].remove(u)
    
    # Use DFS for connectivity check.
    connected = is_connected(graph_copy, u, v)
    
    # Restore the removed edge.
    graph_copy[u].append(v)
    graph_copy[v].append(u)

    return not connected
