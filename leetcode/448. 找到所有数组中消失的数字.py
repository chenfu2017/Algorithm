from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for num in nums:
            index = (num - 1) % n
            nums[index] += n
        for i in range(n):
            if nums[i] <= n:
                res.append(i+1)
        return res


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(Solution().findDisappearedNumbers(nums))
