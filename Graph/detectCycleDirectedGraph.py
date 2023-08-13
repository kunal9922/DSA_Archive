def isCyclicUtils(graph, vertex, visited):
    # If the current vertex is already visited in the current traversal, there is a cycle.
    if visited[vertex] == True:
        return True
    
    flag = False
    # Explore all neighbors of the current vertex
    for i in range(len(graph[vertex])):
        # Recursively check if the neighbor vertex leads to a cycle
        if flag := isCyclicUtils(graph, graph[vertex][i], visited):
            return flag
    
    return flag

def detectCycleDirected(graph, v):
    visited = [False for _ in range(v)]
    flag: bool = False
    # For each vertex, perform DFS to check for a cycle
    for i in range(v):
        visited[i] = True
        # Check if there is a cycle starting from each neighbor of the current vertex
        for j in range(len(graph[i])):
            if flag := isCyclicUtils(graph, graph[i][j], visited):
                return flag
        visited[i] = False
    
    return flag
'''
  0 -----> 1
  |        |
  |        |
  v        v
  4 -----> 3
  |
  v
  2
'''
# Directed graph represented as an adjacency list
graph = [
    [1],    # Vertex 0 is connected to vertex 1
    [],     # Vertex 1 has no outgoing edges
    [1, 3], # Vertex 2 is connected to vertices 1 and 3
    [4],    # Vertex 3 is connected to vertex 4
    [0, 2]  # Vertex 4 is connected to vertices 0 and 2
]
print(detectCycleDirected(graph, 5))