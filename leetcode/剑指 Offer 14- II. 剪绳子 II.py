class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] * (i - j))
                print(dp[i])
            if i < n:
                dp[i] = max(dp[i], i)
        return dp[n] % 1000000007


n = 1000
print(Solution().cuttingRope(n))
