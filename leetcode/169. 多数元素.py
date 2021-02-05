class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 1
        temp = nums[0]
        for i in range(1, len(nums)):
            if temp == nums[i]:
                res += 1
            else:
                res -= 1
                if res < 0:
                    temp = nums[i]
                    res = 0
        return temp


nums =[2,2,1,1,1,2,2]
print(Solution().majorityElement(nums))