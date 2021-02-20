from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.insert(n, float('-inf'))
        nums.insert(0, float('-inf'))

        for index in range(1,n+1):
            if nums[index - 1] < nums[index] > nums[index + 1]:
                return index-1


nums = [-2147483648]
print(Solution().findPeakElement(nums))
