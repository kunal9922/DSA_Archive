'''Graph Coloring to Detect cycle in an undirected graph O(E + V)
0 Not visited
1 Visited 
2 visited and processed
'''
def isCyclicUtil(graph, visited, vertex):
    if visited[vertex] == 2:
        return True
    visited[vertex] = 1
    FLAG = False
    for i in range(len(graph[vertex])):
        if visited[graph[vertex][i]] == 1:
            return True
        if visited[graph[vertex][i]] == 0:
             if FLAG := isCyclicUtil(graph, visited, graph[vertex][i]):
                return True
    visited[vertex] = 2
    return False

def isCyclic(v, graph):
    visited = [0] * v
    for i in range(v):
        if visited[i] == 0:
            if isCyclicUtil(graph, visited, i):
                return True
    return False

# Adjusted graph with 0-indexed vertices
'''
 0--1 -- 2
   / \   |
  /   \  |
 4-----3-5
'''
graph = [
    [1, ],
    [2, 3, 4],
    [1, 3],
    [1, 2, 5],
    [1, 5],
    [3, 4]
]
print(isCyclic(6, graph))
