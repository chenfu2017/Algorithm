class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums)==0:
            return 0
        j = 0
        for i in range(0,len(nums)):
            if nums[i] != val:
                if i!=j:
                    nums[j]=nums[i]
                j += 1
        return j
nums = [0,1,2,2,3,0,4,2]
print(Solution().removeElement(nums, 2))
