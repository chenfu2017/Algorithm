class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j=0,len(nums)-1
        while i<=j:
            mid = (i+j)//2
            if target==nums[mid]:
                m = mid
                n = mid
                while m>0 and nums[m-1]==target:
                    m -=1
                while n<len(nums)-1 and nums[n+1]==target:
                    n +=1
                return [m,n]
            elif target<nums[mid]:
                j = mid -1
            else:
                i = mid +1
        return [-1,-1]

nums = [1]
target = 1
print(Solution().searchRange(nums,target))

