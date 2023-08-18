'''Topological sort t ensures that for every directed edge from vertex A to vertex B,
 vertex A comes before vertex B in the ordering. 
 Time complexity O(V + E), Space O(V) '''
def detecCycle(adj, numCourse):
    return None
#Topological sort
def dfs(graph, vertex, visited, stack):
    if visited[vertex] is True:
        return
    visited[vertex] = True
    for i in range(len(graph[vertex])):
        if visited[graph[vertex][i]] == False:
            dfs(graph, graph[vertex][i], visited, stack)

    stack.append(vertex)
#Course Schedule 
def findOrder(numCourse: int, prerequisites):
    n = len(prerequisites)
    #Making adjacency list
    adj = [[] for _ in range(numCourse)]
    for i in range(n):
        adj[prerequisites[i][1]].append(prerequisites[i][0])

    # Detect Cycle if present then return empty array
    if detecCycle(adj, numCourse):
        return None
    
    #Find topological sort and store it in stack
    stack = []
    visited = [False for _ in range(numCourse)]

    #Apply DFS and find topological sort
    for i in range(numCourse):
        if visited[i] == False:
            dfs(adj, i, visited, stack)
    
    ans = []
    while stack:
        ans.append(stack.pop())
    
    print(ans)


inputGraph = [
    [0, 1, 2, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]

]
findOrder(4, inputGraph)