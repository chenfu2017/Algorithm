from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, sum, l):
            if sum == target:
                l.sort()
                if l not in res:
                    res.append(l)
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if sum + candidates[j] <= target:
                    dfs(j + 1, sum + candidates[j], l + [candidates[j]])

        dfs(0, 0, [])
        return res


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(Solution().combinationSum2(candidates, target))
