from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1,n):
            nums[i] = max(nums[i-1],nums[i] + i)
        index = 0
        while index < n -1:
            ans +=1
            index = nums[index]
        return ans


nums = [2,2,1,1,1]
print(Solution().jump(nums))
