class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        res = 0
        while i < j:
            h = min(height[i], height[j])
            res = max(res, h * (j - i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return res

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
