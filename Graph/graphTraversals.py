#Breath First Search
def bfs(graph, startVertex):
    if graph is None: # empty graph
        return None
    #No. of vertex in a graph to mark them if they visted or not
    vertex = len(graph)
    visited = [False for _ in range(vertex)]
    visited[startVertex] = True
    queue = [startVertex,]
    print(startVertex)

    while queue:
        curV = queue.pop(0)
        # Traversing to its adjacent vertex
        for v in graph[curV]:     
            if visited[v] is False:
                visited[v] = True
                print(v)
                queue.append(v)

# Depth first Search DFS
def dfs(graph, vertex, visited: list):
    if graph is None:
        return None # Empty graph has passed
    #Making that node is visited
    visited[vertex] = True
    print(vertex)
    for i in range(len(graph[vertex])):
        if visited[graph[vertex][i]] == False:
            dfs(graph, graph[vertex][i], visited)
   


graph_adj_list_directed = [
    [1, 2],
    [2, 3, 4],
    [1, 3],
    [2, 4, 5],
    [3, 5],
    [3, 4]
]

print(f'BFS of a Graph : {bfs(graph= graph_adj_list_directed, startVertex= 1)}')

visited = [False for _ in range(len(graph_adj_list_directed))]
print(f'DFS of a graph : {dfs(graph_adj_list_directed, 0, visited)}')