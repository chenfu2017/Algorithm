import bisect


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        n = len(nums)
        f = [nums[0]]
        for i in range(1, n):
            if nums[i] > f[-1]:
                f.append(nums[i])
            else:
                index = bisect.bisect_left(f, nums[i])
                f[index] = nums[i]
        return len(f)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(Solution().lengthOfLIS(nums))
