class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        n = len(nums)
        m = [1] * n
        for i in range(1,n):
            for j in range(0,i):
                if nums[j]<nums[i]:
                    m[i] = max(m[i],1+m[j])
        return max(m)

nums =[10,9,2,5,3,7,101,18]
print(Solution().lengthOfLIS(nums))

