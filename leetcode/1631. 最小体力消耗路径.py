from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        size = m * n
        uf = UnionFind(size)
        edge = []
        for i in range(m):
            for j in range(n):
                index = i * n + j
                if i > 0:
                    edge.append([index - n, index, abs(heights[i][j] - heights[i - 1][j])])
                if j > 0:
                    edge.append([index - 1, index, abs(heights[i][j] - heights[i][j - 1])])
        if len(edge) == 0:
            return 0
        edge.sort(key=lambda e: e[2])
        for e in edge:
            x, y, z = e
            uf.union(x, y)
            if uf.connected(0, size - 1):
                return z


class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = []
        for i in range(n):
            self.parent.append(i)

    def connected(self, x, y):
        x, y = self.find(x), self.find(y)
        return x == y

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return x

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx != rooty:
            self.parent[rootx] = rooty
            self.count -= 1
            return False
        return True

    def getCount(self):
        return self.count


heights =[[1,10,6,7,9,10,4,9]]
print(Solution().minimumEffortPath(heights))
