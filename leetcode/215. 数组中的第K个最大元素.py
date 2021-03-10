from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def find(i, j):
            left = i
            right = j
            temp = nums[i]
            while left < right:
                while left < right and nums[right] >= temp:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] <= temp:
                    left += 1
                nums[right] = nums[left]
            nums[right] = temp
            if k == right:
                return nums[right]
            if k > right:
                return find(right + 1, j)
            else:
                return find(i, right - 1)
        n = len(nums)
        k = n - k
        return find(0, n - 1)


nums = [3, 1]
k = 1
print(Solution().findKthLargest(nums, k))
