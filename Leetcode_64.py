class Solution:
    def minPathSum(self, gird):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(gird) - 1
        m = len(gird[0]) - 1
        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i == n and j == m:
                    continue
                elif i == n:
                    gird[i][j] += gird[i][j + 1]
                elif j == m:
                    gird[i][j] += gird[i + 1][j]
                else:
                    gird[i][j] += min(gird[i][j + 1], gird[i + 1][j])
        return gird[0][0]


gird = [
    [1, 2],
    [5, 6],
    [1, 1]
]
print(Solution().minPathSum(gird))
