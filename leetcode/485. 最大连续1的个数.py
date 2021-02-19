from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for i in nums:
            if i==1:
                count +=1
            else:
                if count > res:
                    res = count
                count = 0
        return max(res,count)






nums = [1,1,0,1,1,1]
print(Solution().findMaxConsecutiveOnes(nums))

