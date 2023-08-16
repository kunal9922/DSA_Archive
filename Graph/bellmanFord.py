import random
from numpy import Inf
'''Bellman-Ford algorithm: 
Finds the shortest paths from a single source vertex to all other vertices in a weighted directed graph,
 even in the presence of negative edge weights, in O(V * E) time complexity'''
class Edge:
    def __init__(self):
        self.src = None
        self.dst = None
        self.wt = None

def bellmanFord(edgeList, V, E):
    parent = [0 for _ in range(V)]
    cost_parent = [0 for _ in range(V)]
    value = [Inf for _ in range(V)]

    # Assuming start point as Node-0
    parent[0] = -1
    value[0] = 0

    updated = False
    # include V-1 edges to cover all V-vertices
    for _ in range(V-1):
        updated = False
        for j in range(E):
            U = edgeList[j].src
            V = edgeList[j].dst
            wt = edgeList[j].wt
            if value[U]!= Inf and value[U] + wt < value[V]:
                value[V] = value[U] + wt
                parent[V] = U
                cost_parent[V] = value[V]
                updated = True
        
        if updated == False:
            break
    for k in range(E):
            U = edgeList[k].src
            V = edgeList[k].dst
            wt = edgeList[k].wt
            if value[U]!= Inf and value[U] + wt < value[V]:
                print("Graph has -VE edge cycle \n") 
                return    
        
# Generate dummy data
V = 5  # Number of vertices
E = 7  # Number of edges

# Generate random edges with weights
edgeList = [Edge() for _ in range(E)]

for i in range(E):
    edgeList[i].src = random.randint(0, V - 1)
    edgeList[i].dst = random.randint(0, V - 1)
    edgeList[i].wt = random.randint(-10, 10)

print("Generated Edge List:")
for i in range(E):
    print(f"Edge {i+1}: Source = {edgeList[i].src}, Destination = {edgeList[i].dst}, Weight = {edgeList[i].wt}")

bellmanFord(edgeList, V, E)
