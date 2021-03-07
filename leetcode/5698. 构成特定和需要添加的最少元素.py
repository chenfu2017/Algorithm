from typing import List


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        total = sum(nums)
        diff = abs(total - goal)
        if diff % limit == 0:
            return diff // limit
        else:
            return diff // limit +1


nums = [-1,0,1,1,1]
limit = 1
goal = 771843707
print(Solution().minElements(nums, limit, goal))
