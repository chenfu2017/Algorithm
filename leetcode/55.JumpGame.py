class Solution:
    def canJump(self, nums):
        for i in range(len(nums)):
            guo = True
            if nums[i] == 0 and i < (len(nums) - 1):
                guo = False
                for j in range(i):
                    if nums[j] > (i - j):
                        guo = True
            if guo == False:
                return False

        return True


nums = [4, 2, 0, 0, 1, 1, 4, 4, 4, 0, 4, 0]
print(Solution().canJump(nums))
