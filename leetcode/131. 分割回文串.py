from typing import List


class Solution:

    def partition(self, s: str) -> List[List[str]]:
        def dfs(index, l):
            if index == n:
                ans.append(l)
                return
            for i in range(index, n):
                if dp[index][i]:
                    dfs(i + 1, l + [s[index:i + 1]])

        ans = []
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for right in range(n):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True
        dfs(0,[])
        return ans


s = "aab"
print(Solution().partition(s))
