from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:

        m = len(nums)
        n = len(nums[0])
        if m * n != r * c:
            return nums
        res = [[0] * c for _ in range(r)]
        count = 0
        row = 0
        for i in range(m):
            for j in range(n):
                if count >= c:
                    row +=1
                    count = 0
                res[row][count] = nums[i][j]
                count +=1
        return res


nums = [[1, 2],
        [3, 4]]
r = 1
c = 4
print(Solution().matrixReshape(nums, r, c))
