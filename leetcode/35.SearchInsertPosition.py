class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return 0
        i =0
        while i<len(nums):
            if nums[i]>=target:
                break
            i +=1
        return i

nums=[1,3,5,6]
target=2
print(Solution().searchInsert(nums,target))