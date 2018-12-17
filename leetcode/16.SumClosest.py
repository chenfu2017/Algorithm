class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = 999999
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                l, r = i + 1, len(nums) - 1
                while l < r:
                    tmp_res = target - nums[i] - nums[l] - nums[r]
                    if abs(tmp_res) < res:
                        res = abs(tmp_res)
                        ret = nums[i] + nums[l] + nums[r]
                    if tmp_res < 0:
                        while l < r and nums[r - 1] == nums[r]:
                            r -= 1
                        r -= 1
                    elif tmp_res > 0:
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        l += 1
                    else:
                        return target
        return ret

nums = [-1, 2, 1, -4]
target = 1
print(Solution().threeSumClosest(nums, target))
