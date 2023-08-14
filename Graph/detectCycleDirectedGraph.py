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
0 -------> 1 ----->2
^          |       |
|          |       |
|          v       v
4 <------- 3-----> 5
'''
# Directed graph represented as an adjacency list
graph = {
    0: [1,],
    1: [2, 3],
    2: [5,],
    3: [4, 5],
    4: [0,],
    5: []
}

print(detectCycleDirected(graph, 6))