class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        l = [([0] * m) for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    l[i][j] = 1
                else:
                    l[i][j] = l[i - 1][j] + l[i][j - 1]
        return l[n-1][m-1]


print(Solution().uniquePaths(7, 3))
