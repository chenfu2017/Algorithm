from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for j in range(n):
            for i in range(j + 1):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
        ans = []

        def dfs(i, l):
            if i == n:
                ans.append(l.copy())
                return
            for j in range(i, n):
                if dp[i][j]:
                    dfs(j + 1, l + [s[i:j + 1]])

        dfs(0, [])
        return ans


s = "abbab"
print(Solution().partition(s))
