'''Clone an Undirected Graph using Hash Map'''
class Vertex:
    def __init__(self, val = 0, edges = None):
        self.val = val
        self.edges = edges if edges is not None else []

class Clone:
    def cloneGraph(self, vertex: Vertex) -> Vertex:
        oldToNew = {} #Dictonary contains the vertex that has created 

        def dfs(vertex: Vertex):
            if vertex in oldToNew:
                return oldToNew[vertex]
            copy = Vertex(vertex.val)
            oldToNew[vertex] = copy
            # iterate to adjacents vertex
            for adj in vertex.edges:
                copy.edges.append(dfs(adj))
            return copy
        
        return dfs(vertex) if vertex else None

def printGraphDFS(visited, vertex: Vertex):
    if visited[vertex.val] is True:
        return 
    visited[vertex.val] = True
    print(vertex.val)
    for adj in vertex.edges:
        if visited[adj.val] is False:
            printGraphDFS(visited, adj)

# Create graph with values
graph = [Vertex(i) for i in range(1, 6)]  # Creating 5 graph with values 1 to 5

# Create edges (undirected)
graph[0].edges.append(graph[1])
graph[1].edges.append(graph[0])

graph[1].edges.append(graph[2])
graph[2].edges.append(graph[1])

graph[2].edges.append(graph[3])
graph[3].edges.append(graph[2])

# Access neighbors of a vertex
print("Edges of vertex 2:", [neighbour.val for neighbour in graph[1].edges])

deepCopy = Clone()
cloneGraph = deepCopy.cloneGraph(graph[0])

visited = [False for _ in range(1, 6)]
printGraphDFS(visited, cloneGraph)
