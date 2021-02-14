from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = twice = 0
        for x in nums:
            once = (once ^ x) & (~twice)
            twice = (twice ^ x) & (~once)
        return once


l = [2, 2, 1, 4, 4, 4, 1, 1, 2, 6]
print(Solution().singleNumber(l))
