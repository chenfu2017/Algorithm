class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        N = len(grid)
        M = len(grid[0])
        size = N * M
        UF = UnionFind(size)
        count = 0
        for i in range(N):
            l = grid[i]
            for j in range(M):
                index = i * M + j
                s = l[j]
                if s == '1':
                    if j + 1 < M and l[j + 1] == '1':
                        UF.union(index, index + 1)

                    if i + 1 < N and grid[i + 1][j] == '1':
                        UF.union(index, (i + 1) * M + j)
                else:
                    count += 1
        # print(UF.count)
        # print(count)
        return UF.count - count


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
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(Solution().numIslands(grid))
