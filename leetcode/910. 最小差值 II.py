from typing import List


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        ans = A[-1] - A[0]
        n = len(A) - 1
        for i in range(n):
            maxnum = max(A[i] + K, A[n] - K)
            minnum = min(A[0] + K, A[i + 1] - K)
            ans = min(ans, maxnum - minnum)
        return ans


A = [3, 1, 10]
K = 4
print(Solution().smallestRangeII(A, K))
