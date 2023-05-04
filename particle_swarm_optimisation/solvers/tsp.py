import itertools
import sys

def tsp(graph):
    # Create a set of all the nodes in the graph
    nodes = set(range(len(graph)))
    
    # Create a dictionary to store the shortest path between two nodes
    # Initialize it to the maximum integer value
    shortest_paths = {(i, j): sys.maxsize for i in nodes for j in nodes if i != j}
    
    # Calculate the shortest path between two nodes using the Euclidean distance
    for i, j in itertools.combinations(nodes, 2):
        distance = ((graph[i][0] - graph[j][0]) ** 2 + (graph[i][1] - graph[j][1]) ** 2) ** 0.5
        shortest_paths[(i, j)] = distance
        shortest_paths[(j, i)] = distance
    
    # Create a dictionary to store the shortest path from a node to a subset of nodes
    # Initialize it to the maximum integer value
    shortest_path_subset = {(i, frozenset([i])): 0 for i in nodes}
    
    # Calculate the shortest path from a node to a subset of nodes
    for size in range(2, len(nodes) + 1):
        for subset in itertools.combinations(nodes, size):
            subset = frozenset(subset)
            for i in subset:
                subset_without_i = subset - {i}
                shortest_path_subset[(i, subset)] = min(shortest_path_subset[(j, subset_without_i)] + shortest_paths[(i, j)] for j in subset_without_i)
    
    # Calculate the shortest path that visits all the nodes exactly once
    all_nodes = frozenset(nodes)
    shortest_path = min(shortest_path_subset[(i, all_nodes)] + shortest_paths[(i, 0)] for i in range(1, len(graph)))
    
    return shortest_path
