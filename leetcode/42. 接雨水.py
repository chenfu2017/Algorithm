from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        res = 0
        left_max = right_max = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    res += left_max - height[left]
                left +=1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -=1
        return res


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))
