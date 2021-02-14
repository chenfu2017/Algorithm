from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = count = 1
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                count +=1
            else:
                count = 1
            if count <3:
                nums[j] = nums[i]
                j +=1
        # print(nums)
        return j


nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(Solution().removeDuplicates(nums))
