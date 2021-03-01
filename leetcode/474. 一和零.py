from typing import List


class Solution:

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(l + 1)]
        for i in range(1, l + 1):
            for j in range(m + 1):
                for k in range(n + 1):
                    count1 = strs[i - 1].count('0')
                    count2 = len(strs[i - 1]) - count1
                    if j < count1 or k < count2:
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - count1][k - count2] + 1)
        return dp[l][m][n]


strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
print(Solution().findMaxForm(strs, m, n))
