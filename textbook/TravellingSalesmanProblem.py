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

    def travel(self,index, c, cx):
        n = len(self.G)
        if index == n - 1:
            c += self.G[cx[-1]][cx[0]]
            if c < self.res:
                self.x = cx.copy()
                self.res = c
            return
        for i in range(n):
            if not self.visited[i]:
                self.visited[i] = True
                self.travel( index + 1, c + self.G[cx[-1]][i], cx + [i])
                self.visited[i] = False


s = Solution()
s.visited[0] = True
s.travel(0, 0, [0])
print(s.res)
