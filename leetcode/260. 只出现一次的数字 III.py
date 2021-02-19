from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        temp = nums[0]
        for num in nums[1:]:
            temp ^= num
        div = 1
        while div & temp == 0:
            div <<= 1
        a = b = 0
        for num in nums:
            if num & div:
                a ^= num
            else:
                b ^= num
        return [a, b]


nums = [1, 2, 1, 3,3]
print(Solution().singleNumber(nums))
