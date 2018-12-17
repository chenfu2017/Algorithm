class Solution:
    visited = []
    d = [[0, 1], [-1, 0], [1, 0], [0, -1]]

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        if len(grid)==0:
            return res
        self.visited.clear()
        l = [False] * len(grid[0])
        for i in range(len(grid)):
            self.visited.append(l.copy())
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and not self.visited[i][j]:
                    res += 1
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, x, y):
        self.visited[x][y] = True
        for i in self.d:
            newx = x + i[0]
            newy = y + i[1]
            # print('(%s,%s)' % (newx, newy))
            if newx >= 0 and newy >= 0 and newx < len(grid) and newy < len(grid[0]) \
                    and not self.visited[newx][newy] and grid[newx][newy] == '1':
                self.dfs(grid, newx, newy)
        return


grid = [["1", "1", "1", "1", "0"],
        ["0", "0", "0", "0", "0"],
        ["1", "1", "1", "1", "0"],
        ["0", "0", "0", "0", "0"],
        ]

grid = []
print(Solution().numIslands(grid))
