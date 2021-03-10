from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        n = len(nums)

        def dfs(i, l):
            if i == n:
                s = sorted(l)
                if s not in ans:
                    ans.append(s)
                return
            dfs(i+1, l + [nums[i]])
            dfs(i+1, l)

        dfs(0, [])
        return ans


nums = [1, 2, 3]
# [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
print(Solution().subsetsWithDup(nums))
