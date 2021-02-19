from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        left = 0
        right = 0
        res = 0
        count = 0
        while right < n:
            if A[right] == 0:
                count += 1
            if count <= K:
                res = max(res, right - left+1)
            else:
                while A[left] == 1:
                    left += 1
                left += 1
                count -= 1
            right += 1
        return res


A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3
print(Solution().longestOnes(A, K))
