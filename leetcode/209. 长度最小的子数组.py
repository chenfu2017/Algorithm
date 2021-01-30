class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = n + 1
        start = 0
        end = 0
        sum = 0
        while end < n:
            sum += nums[end]
            while sum >= s:
                ans = min(ans, end - start + 1)
                sum -= nums[start]
                start += 1
            end += 1
        return 0 if ans == n + 1 else ans


s = 11
nums = [1, 2, 3, 4, 5]
print(Solution().minSubArrayLen(s, nums))
