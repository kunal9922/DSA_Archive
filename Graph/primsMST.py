# Prims Minimum spanning tree Time O(V^2)
import numpy as np

class MinSpanningTree:
    def picMinVertex(self, distance: list, mst: list):
        mini = np.Inf
        idx = None
        for i, item in enumerate(distance):
            if item < mini and i not in mst:
                mini = item
                idx = i
        return idx

    def prims(self, graph):
        dis  = [np.Inf for _ in range(len(graph))]
        dis[0] = 0  # Starting point of the graph
        mstSet = set()  # Minimum spanning tree set
        parent = [-1 for _ in range(len(graph))]  # Parent array to store MST edges
        rows = len(graph)
        columns = len(graph[0])

        for _ in range(rows-1):
            curVertex = self.picMinVertex(dis, mstSet)
            mstSet.add(curVertex)
            for j in range(columns):
                if graph[curVertex][j] != 0 and j not in mstSet and graph[curVertex][j] < dis[j]:
                    dis[j] = graph[curVertex][j]
                    parent[j] = curVertex

        # Print MST edges and weights
        for i in range(rows):
            print(f"U -> V: {parent[i]} -> {i} wt = {dis[i]}")

graph = [
    [0, 4, 6, 0, 0, 0],
    [4, 0, 6, 3, 4, 0],
    [6, 6, 0, 1, 0, 0],
    [0, 3, 1, 0, 2, 3],
    [0, 4, 0, 2, 0, 7],
    [0, 0, 0, 3, 7, 0]
]

prims = MinSpanningTree()
prims.prims(graph)
