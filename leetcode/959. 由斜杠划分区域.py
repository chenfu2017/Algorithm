class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """

        N = len(grid)

        UF = UnionFind(4 * N * N)
        for i in range(N):
            strstr = grid[i]
            for j in range(N):
                index = 4 * (i * N + j)
                c = strstr[j]
                if c == ' ':
                    UF.union(index, index + 1)
                    UF.union(index + 1, index + 2)
                    UF.union(index + 2, index + 3)
                elif c == '/':
                    UF.union(index, index + 3)
                    UF.union(index + 1, index + 2)
                else:
                    UF.union(index, index + 1)
                    UF.union(index + 2, index + 3)
                if j + 1 < N:
                    UF.union(index + 1, 4 * (i * N + j + 1) + 3)
                if i + 1 < N:
                    UF.union(index + 2, 4 * ((i + 1) * N + j))

        # UF.output()
        return UF.getCount()


class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = []
        for i in range(n):
            self.parent.append(i)

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

    def getCount(self):
        return self.count

grid = [
    "/\\",
    "\\/"
]
print(Solution().regionsBySlashes(grid))
