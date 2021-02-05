class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        for i in range(res):
            res ^= i ^ nums[i]
        return res

nums = [3,0,1]
print(Solution().missingNumber(nums))