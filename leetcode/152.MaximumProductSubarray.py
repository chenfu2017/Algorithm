class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        arr_min = [float("inf")] * l
        arr_max = [float("-inf")] * l
        arr_min[0] = arr_max[0] = nums[0]
        for i in range(1,l):
            m = arr_max[i - 1] * nums[i]
            n = arr_min[i - 1] * nums[i]
            arr_min[i] = min(m, n,nums[i])
            arr_max[i] = max(m, n,nums[i])
        return max(arr_max)

nums = [-2,0,-1]
print(Solution().maxProduct(nums))
