import time
class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        s = sum(nums)
        m = max(nums)
        if s % 2 or 2 * m > s: return False
        C = s // 2
        m = [False] * (C+1)
        for i in range(C+1):
            m[i] = (nums[0]==i)
        print(m)
        for i in range(1,n):
            for j in range(C,nums[i]-1,-1):
                m[j] = m[j] or m[j-nums[i]]
        return m[C]

c = Solution()
nums=[2000,2222,7,3,4,5,6,7]
start =time.clock()
print(c.canPartition(nums))
end = time.clock()
print('Running time: %s Seconds'%(end-start))

