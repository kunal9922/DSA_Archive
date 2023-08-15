from numpy import Inf
# Detect Negative edge weight cycle
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
    for i in range(V-1):
        updated = False
        for _ in range(E):
            U = edgeList[i].src
            V = edgeList[i].dst
            wt = edgeList[i].wt
            if value[U]!= Inf and value[U] + wt < value[V]:
                value[V] = value[U] + wt
                parent[V] = U
                cost_parent[V] = value[V]
                updated = True
        
        if updated == False:
            break
    for _ in range(E):
            U = edgeList[i].src
            V = edgeList[i].dst
            wt = edgeList[i].wt
            if value[U]!= Inf and value[U] + wt < value[V]:
                print("Graph has -VE edge cycle \n") 
                return    
        

E = int(input("No. of edges"))
V = int(input("No. of Vertex"))

edgeList = [Edge() for _ in range(E)]

for i in range(E):
    edgeList[i].src = int(input("Source"))
    edgeList[i].dst = int(input("destination"))
    edgeList[i].wt = int(input("Weight"))

bellmanFord(edgeList, V, E)