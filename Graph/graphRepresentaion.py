# Graph Representation
def are_graphs_identical(adj_matrix, adj_list):
    n = len(adj_matrix)
    # Check if the number of vertices in the adjacency list matches the adjacency matrix
    if len(adj_list) != n:
        return False
    # Iterate through each vertex
    for i in range(n):
        # Check if the number of neighbors in the adjacency list matches non-zero entries in the matrix
        if len(adj_list[i]) != sum(1 for j in range(n) if adj_matrix[i][j] != 0):
            return False
        # Check if the neighbors listed in the adjacency list match non-zero entries in the matrix
        for j in range(n):
            if adj_matrix[i][j] != 0 and j not in adj_list[i]:
                return False
    
    return True
#Adjacency Matrix and list Directed
graph_adj_matrix_directed = [
    [0, 4, 6, 0, 0, 0],
    [0, 0, 6, 3, 4, 0],
    [0, 6, 0, 1, 0, 0],
    [0, 0, 1, 0, 2, 3],
    [0, 0, 0, 2, 0, 7],
    [0, 0, 0, 3, 7, 0]
]

graph_adj_list_directed = [
    [1, 2],
    [2, 3, 4],
    [1, 3],
    [2, 4, 5],
    [3, 5],
    [3, 4]
]

# Adjacency matrix and list Undirected
graph_adj_matrix = [
    [0, 4, 6, 0, 0, 0],
    [4, 0, 6, 3, 4, 0],
    [6, 6, 0, 1, 0, 0],
    [0, 3, 1, 0, 2, 3],
    [0, 4, 0, 2, 0, 7],
    [0, 0, 0, 3, 7, 0]
]

graph_adj_list = [
    [1, 2],
    [0, 2, 3, 4],
    [0, 1, 3],
    [1, 2, 4, 5],
    [1, 3, 5],
    [3, 4]
]
# Call the function to check if the graphs are identical
if result := are_graphs_identical(graph_adj_matrix, graph_adj_list):
    print("The adjacency matrix and adjacency list represent the same graph.")
else:
    print("The adjacency matrix and adjacency list do not represent the same graph.")
