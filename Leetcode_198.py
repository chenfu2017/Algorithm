class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==0:
            return 0
        m = [-1] * n
        m[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            for j in range(i,n):
                m[i] = max(m[i],nums[j]+(m[j+2] if(j+2<n) else 0))
        return m[0]

nums=[1,2,3,1]
print(Solution().rob(nums))



