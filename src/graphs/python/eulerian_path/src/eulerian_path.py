# Import the is_connected and is_bridge functions
from is_connected import is_bridge, is_connected

# Implement the Fleury algorithm using a function named eulerian_path
# The function takes a graph as a parameter
# the function returns the eulerian path as list
def eulerian_path(graph):
    # Create a copy of the graph
    graph_copy = {u: list(neighbors) for u, neighbors in graph.items()}

    # Calculate Odd-Degree Nodes for an Eulerian Path
    odd_degree_nodes = [u for u in graph if len(graph[u]) % 2 != 0]

    # Check Eulerian Path Second Condition
    if len(odd_degree_nodes) != 0 and len(odd_degree_nodes) != 2:
        return "No Eulerian path exists"

    # Choose a starting node
    # The use of next(iter(graph)) here to handle the case of big graphs
    start_node = odd_degree_nodes[0] if odd_degree_nodes else next(iter(graph))

    path = [start_node]
    #current_node = start_node

    while graph_copy:
        current_node = path[-1]
        for neighbor in graph_copy[path[-1]]:
            if not is_bridge(path[-1], neighbor, graph_copy):
                # Remove the edge
                graph_copy[path[-1]].remove(neighbor)
                graph_copy[neighbor].remove(path[-1])
                # Move to the next vertex
                path.append(neighbor)
                break

        if path[-1] == current_node:
            # This means we have not moved to a new vertex
            break


    return path


