class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s = sum(nums[:k])
        res = s
        for i in range(k, len(nums)):
            s = s + nums[i] - nums[i - k]
            if s > res:
                res = s
        return res / k


nums = [1, 12, -5, -6, 50, 3]
k = 4
print(Solution().findMaxAverage(nums, k))
