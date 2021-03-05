class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for j in range(2, n + 1):
            for i in range(j - 1, -1, -1):
                ans = float('inf')
                for k in range(i, j):
                    ans = min(ans, k + max(dp[i][k - 1], dp[k + 1][j]))
                dp[i][j] = ans
        return dp[0][n]


n = 10
print(Solution().getMoneyAmount(n))
