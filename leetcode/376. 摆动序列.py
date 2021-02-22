from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        prevdiff = nums[1] - nums[0]
        ans = 2 if prevdiff != 0 else 1
        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if diff > 0 >= prevdiff or diff < 0 <= prevdiff:
                ans += 1
                prevdiff = diff
        return ans


nums = [0, 0, 0,1]
print(Solution().wiggleMaxLength(nums))
