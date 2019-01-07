class Solution:
    def __init__(self):
        INF = float('INF')
        self.G = [
            [INF, 5, 9, 4],
            [5, INF, 13, 2],
            [9, 13, INF, 7],
            [4, 2, 7, INF],
        ]
        self.visited = [False] * len(self.G)
        self.res = INF
        self.x = []
        self.count = 0

    def travel_1(self, index, c, cx):
        n = len(self.G)
        if index == n - 1:
            c += self.G[cx[-1]][cx[0]]
            if c < self.res:
                self.x = cx.copy()
                self.res = c
            return
        for i in range(n):
            self.count += 1
            if not self.visited[i] and c + self.G[cx[-1]][i] < self.res:
                self.visited[i] = True
                self.travel_1(index + 1, c + self.G[cx[-1]][i], cx + [i])
                self.visited[i] = False

    def travel_2(self, s, c, cx):
        n = len(self.G)
        if s == n:
            c += self.G[cx[-1]][cx[0]]
            if c < self.res:
                self.res = c
                self.x = cx.copy()
            return
        for i in range(s, n):
            self.count += 1
            if self.G[cx[i - 1]][cx[i]] != 0 and c + self.G[cx[i - 1]][cx[i]] < self.res:
                cx[i], cx[s] = cx[s], cx[i]
                self.travel_2(s + 1, c + self.G[cx[s - 1]][cx[s]], cx)
                cx[i], cx[s] = cx[s], cx[i]


s = Solution()
start = 3
s.visited[start] = True
# s.travel_1(0, 0, [start])
s.travel_2(1, 0, [0, 1, 2, 3])
print(s.res)
print(s.count)
