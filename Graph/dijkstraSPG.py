from numpy import Inf
def selectMinVertex(dis, processed):
    mini = Inf
    idx = None
    for i, item in enumerate(dis):
        if item < mini and processed[i] == False:
            mini = item
            idx = i
    return idx
# Time O(v^2) Simpler implementation
# Adj list + min_heap O(E logV)
def dijkstra(graph):
    V = len(graph) # No. of vertices 
    parent = [None for _ in range(V)]
    dis = [Inf for _ in range(V)]
    processed = [False for _ in range(V)]


    # assuming start point as Node-0
    parent[0] = -1 
    dis[0] = 0

    # Include (V-1) edges to cover all V-vertices
    for _ in range(V-1):
        U = selectMinVertex(dis, processed)
        processed[U] = True
        # Relax adjacent vertices (Not yet included in Shortest Path Graph)
        for j in range(V):
            '''3 conditions to relax:-
            1. Edge is present from U to j.
            2. Vertex j is not included in shortest path graph
            3. Edge weight is smaller than current edge weight
            '''
            if (graph[U][j] != 0) & (processed[j] == False) & (dis[U] != Inf) & (dis[U] + graph[U][j] < dis[j]):
                dis[j] = dis[U] + graph[U][j]
                parent[j] = U
    
    # print mst 
    for i in range(V):
        print(f"U -> V: {parent[i]} -> {i} wt = {dis[i]}")  


graph = [
    [0, 1, 4, 0, 0, 0],
    [1, 0, 4, 2, 7 ,0],
    [4, 4, 0, 3, 5, 0],
    [0, 2, 3, 0, 4, 6],
    [0, 7, 5, 4, 0, 7],
    [0, 0, 0, 6, 7, 0]
]
dijkstra(graph=graph)