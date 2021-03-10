from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def dfs(cur, temp, sum):
            if len(temp) + 10 - cur < k or len(temp) > k:
                return
            if len(temp) == k and sum == n:
                ans.append(temp)
                return
            dfs(cur + 1, temp + [cur], sum + cur)
            dfs(cur + 1, temp, sum)
        dfs(1, [], 0)
        return ans


k = 3
n = 9
print(Solution().combinationSum3(k, n))
