class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = sum(nums)
        s = 0
        for i in range(n):
            if 2 * s + nums[i] == total:
                return i
            s += nums[i]
        return -1


nums = [1, 7, 3, 6, 5, 6]
print(Solution().pivotIndex(nums))
