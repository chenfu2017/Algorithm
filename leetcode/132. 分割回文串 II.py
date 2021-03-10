class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for j in range(n):
            for i in range(j + 1):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
        f = [float('inf')] * n
        for i in range(n):
            if dp[0][i]:
                f[i] = 0
            else:
                for j in range(i):
                    if dp[j+1][i]:
                        f[i] = min(f[i],f[j]+1)
        return f[-1]


s = "abacabac"
print(Solution().minCut(s))
