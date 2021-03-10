class Solution:
    def waysToChange(self, n: int) -> int:
        l = [1,5,10,25]
        dp = [1] + [0] * n
        for i in l:
            for j in range(i,n+1):
                dp[j] = dp[j] + dp[j-i]
        return dp[n] % 1000000007

n = 10
print(Solution().waysToChange(n))