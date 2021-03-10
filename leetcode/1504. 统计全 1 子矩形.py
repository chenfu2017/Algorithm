from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        ans = 0
        rows = len(mat)
        columns = len(mat[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if j == 0:
                    dp[i][j] = mat[i][j]
                elif mat[i][j] == 1:
                    dp[i][j] = dp[i][j - 1] + 1
                mincol = float('inf')
                for k in range(i, -1, -1):
                    mincol = min(mincol, dp[k][j])
                    ans += mincol
        return ans


mat = [[1, 0, 1],
       [1, 1, 0],
       [1, 1, 0]]

print(Solution().numSubmat(mat))
