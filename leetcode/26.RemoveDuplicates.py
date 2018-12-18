class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        j =0
        last = nums[0]
        for i in range(1,len(nums)):
            if nums[i]!=last:
                j += 1
                nums[j]= nums[i]
                last = nums[i]
        return j+1



print(Solution().removeDuplicates([]))