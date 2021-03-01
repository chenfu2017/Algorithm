from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(1, len(nums)):
            self.nums[i] = self.nums[i - 1] + self.nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j] - (self.nums[i - 1] if i > 0 else 0)


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))
