class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums == None:
            return 0
        n = len(nums)
        if n==0:
            return 0
        m = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                m[i] = m[i - 1] + 1
            else:
                m[i] = 1
        return max(m)


nums = [1,2,3,4]
print(Solution().findLengthOfLCIS(nums))
