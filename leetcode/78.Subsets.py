class Solution:
    res = []
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res.clear()
        self.dps(nums,0,[])
        return self.res

    def dps(self,nums,index,tmp):
        self.res.append(tmp)
        for i in range(index,len(nums)):
            self.dps(nums,i+1,tmp+[nums[i]])


nums = [1,2,3]
print(Solution().subsets(nums))