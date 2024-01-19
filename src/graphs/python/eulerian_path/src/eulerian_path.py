# Import the is_connected and is_bridge functions
from is_connected import is_bridge, is_connected

# Implement the Fleury algorithm using a function named eulerian_path
# The function takes a graph as a parameter
# the function returns the eulerian path as list
def eulerian_path(graph):
    # Create a copy of the graph
    graph_copy = {}
    for u, neighbors in graph.items():
        graph_copy[u] = list(neighbors)  # Using list() to create a copy of the neighbors

    # Calculate Odd-Degree Nodes for an Eulerian Path
    odd_degree_nodes = [u for u in graph if len(graph[u]) % 2 != 0]

    # Check Eulerian Path  Second Condition
    if len(odd_degree_nodes) != 2:
        return "No Eulerian path exists"


    # Choose a starting node
    # The use of next(iter(graph)) here to handle the case of big graphs
    start_node = odd_degree_nodes[0] if odd_degree_nodes else next(iter(graph))

    path = []
    current_node = start_node

    while graph_copy:
        for neighbor in graph_copy[current_node]:
            if not is_bridge(current_node, neighbor):
                # Remove the edge
                graph_copy[current_node].remove(neighbor)
                graph_copy[neighbor].remove(current_node)
                # Move to the next vertex
                current_node = neighbor
                path.append((current_node, neighbor))
                break

        if current_node == start_node:
            break

    return path
