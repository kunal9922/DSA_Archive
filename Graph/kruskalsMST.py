# Kruskal's Minimum Spanning Tree algorithm using Union-Find
class KruskalMST:
    def find(self, parent, vertex):
        if parent[vertex] == vertex:
            return vertex
        return self.find(parent, parent[vertex])

    def union(self, parent, rank, vertex1, vertex2):
        root1 = self.find(parent, vertex1)
        root2 = self.find(parent, vertex2)

        if rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            if rank[root1] == rank[root2]:
                rank[root1] += 1

    def kruskal(self, graph):
        edges = []
        rows = len(graph)

        for i in range(rows):
            for j in range(i + 1, rows):
                if graph[i][j] != 0:
                    edges.append((graph[i][j], i, j))

        edges.sort()  # Sort edges based on weights

        parent = [i for i in range(rows)]
        rank = [0] * rows

        minimum_spanning_tree = []
        for weight, u, v in edges:
            if self.find(parent, u) != self.find(parent, v):
                self.union(parent, rank, u, v)
                minimum_spanning_tree.append((u, v, weight))

        return minimum_spanning_tree

graph = [
    [0, 4, 6, 0, 0, 0],
    [4, 0, 6, 3, 4, 0],
    [6, 6, 0, 1, 0, 0],
    [0, 3, 1, 0, 2, 3],
    [0, 4, 0, 2, 0, 7],
    [0, 0, 0, 3, 7, 0]
]

kruskal = KruskalMST()
minimum_spanning_tree = kruskal.kruskal(graph)
print("Edges in Minimum Spanning Tree:")
for u, v, weight in minimum_spanning_tree:
    print(f"U -> V: {u} -> {v} wt = {weight}")
