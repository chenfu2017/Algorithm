class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        m = {}
        for i in range(n):
            for j in range(i + 1, n):
                k = nums[i] * nums[j]
                if k in m:
                    m[k] += 1
                else:
                    m[k] = 1
        ans = 0
        for i in m:
            ans += m[i] * (m[i] - 1) << 2
        return ans


nums = [2, 3, 4, 6, 8, 12]
print(Solution().tupleSameProduct(nums))
