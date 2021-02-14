from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1,len(nums)):
            res ^= nums[i]
        return res


l=[2, 2, 1,4,1]
print(Solution().singleNumber(l))