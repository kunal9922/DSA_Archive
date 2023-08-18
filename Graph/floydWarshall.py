# Floyd Warshall Algorithm is an All pain shortest path
# Time O(V^3) Space o(V^2)
from numpy import Inf

def floyd_warshall(graph, V: int):
    # Assign all values of graph to allPair_SP
    dist = [[graph[i][j]for j in range(V)]for i in range(V)]
    #Find all pairs shortest path by trying all possible paths
    for k in range(V): # Try all intermediate nodes
        for i in range(V): # Try for all possible starting position
            for j in range(V): # Try for all possible ending position
                #Skip if k is unreachable from i or j is unrachable from k
                if dist[i][k] == Inf or dist[k][j] == Inf:
                    continue
                elif dist[i][k] + dist[k][j] < dist[i][j]: # Check if new distance is shorter via vertex k
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Check for negative edge weight cycle
    for i in range(V):
        if dist[i][i] < 0:
            print("Negative Edge Weight cycle is present")
            return 

    # Print the shoretest path graph 
    for i in range(V):
        for j in range(V):
            print(f"{i} to {j} distance is {dist[i][j]}")
        print("====================")

graph = [
    [0, 1, 4, Inf, Inf, Inf],
    [Inf, 0, 4, 2, 7, Inf],
    [Inf, Inf, 0, 3, 4, Inf],
    [Inf, Inf, Inf, 0, Inf, 4],
    [Inf, Inf, Inf, 3, 0, Inf],
    [Inf, Inf, Inf, Inf, 5, 0]
]

floyd_warshall(graph, 6)