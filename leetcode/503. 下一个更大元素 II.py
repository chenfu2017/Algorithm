from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []
        for i in range(2 * n - 1):
            while stack and nums[stack[-1]] < nums[i % n]:
                ans[stack.pop()] = nums[i % n]
            stack.append(i % n)
        return ans


nums = [1, 2, 1]
print(Solution().nextGreaterElements(nums))
