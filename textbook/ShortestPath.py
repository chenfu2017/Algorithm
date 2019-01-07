import queue


class Solution:
    def min_path(self, G, start):
        q = queue.PriorityQueue()
        node = [0, start]
        q.put(node)
        n = len(G)
        dist = [float('INF')] * n
        p = [None] * n
        visited = [False] * n
        while not q.empty():
            d, v = q.get()
            visited[v] = True
            for w in range(n):
                if not visited[w] and d + G[v][w] < dist[w]:
                    dist[w] = d + G[v][w]
                    node = [dist[w], w]
                    p[w] = v
                    q.put(node)
        return dist


INF = float('INF')
G = [
    [0, INF, 10, INF, 30, 100],
    [INF, 0, 4, INF, INF, INF],
    [INF, INF, 0, 50, INF, INF],
    [INF, INF, INF, 0, INF, 10],
    [INF, INF, INF, 20, 0, 60],
    [INF, INF, INF, INF, INF, 0]

]
print(Solution().min_path(G, 0))
