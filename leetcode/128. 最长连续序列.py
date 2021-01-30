class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num_set = set(nums)
        res = 0
        for num in num_set:
            if num - 1 not in num_set:
                temp = 1
                while num + 1 in num_set:
                    temp += 1
                    num += 1
                res = max(res, temp)
        return res


nums = [-10 ** 9, -10 ** 9 + 1, 200, 1, 3, 2,4,0]
print(Solution().longestConsecutive(nums))
