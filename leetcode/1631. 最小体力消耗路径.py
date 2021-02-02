class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        size = n * n
        uf = UnionFind(size)
        edge = []
        for i in range(n):
            for j in range(n):
                index = i * n + j
                if i > 0:
                    edge.append([index - n, index, max(grid[i][j], grid[i - 1][j])])
                if j > 0:
                    edge.append([index - 1, index, max(grid[i][j], grid[i][j - 1])])
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

grid= [[0,2],[1,3]]
print(Solution().swimInWater(grid))