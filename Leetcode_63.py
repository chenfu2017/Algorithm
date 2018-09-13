class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        l = [([0] * n) for i in range(m)]
        for i in range(0,m):
            for j in range(0,n):
                    if obstacleGrid[i][j] == 0:
                        l[i][j] = l[i - 1][j] + l[i][j - 1] if i > 0 or j > 0 else 1
        return l[-1][-1]


obstacleGrid = [
    [0, 0, 0],
    [0, 1, 1],
    [0, 0, 0]
]

print(Solution().uniquePathsWithObstacles(obstacleGrid))
