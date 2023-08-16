from numpy import Inf
class Qnode:
    vertex = None
    dist = None

#Network Delay Time Leetcode #743
#Time complexity = O(V + E) and Space O(V)
def networkDelayTime(times, V, K):
    queue = [] # store in the order of  (vetex, time)
    dist = [Inf for _ in range(V)]
    # Now set to Kth node to dis zero for the selection
    dist[K-1] = 0
    time = 0 #time taken

    qn = Qnode()
    qn.vertex = K
    qn.dist = 0
    queue.append(qn)
    #Simply apply the DFS by using Dijkstra methodology
    while queue:
        cur = queue[0]
        queue.remove(cur) # now take the element from the queue
        for v, d in times[cur.vertex]: # Traversing to all of its adjacents
            qn = Qnode()
            qn.vertex = v
            qn.dist = d + cur.dist
            if (qn.dist < dist[v-1]):
                queue.append(qn)
                dist[v-1] = qn.dist

    #Find the max distance node(if all the nodes are traversal)
    for d in dist:
        if d == Inf:
            return -1
        time = max(time, d)
    return time



graph = {
    1: [(2, 1), (3, 2)],
    2: [(4, 4), (5, 5)],
    3: [(5, 3)],
    4: [(4, 0)],
    5: [(5, 0)]
}

print(networkDelayTime(graph, 5, 1))