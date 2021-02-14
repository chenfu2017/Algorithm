from typing import List


class Solution:
    def atMostKDistinct(self, A, K):
        res = 0
        N = len(A)
        m = [0] * (N + 1)
        i = j = 0
        count = 0
        while j < N:
            if m[A[j]] == 0:
                count += 1
            m[A[j]] += 1
            while count > K:
                m[A[i]] -= 1
                if m[A[i]] == 0:
                    count -= 1
                i += 1
            res += j - i
            j += 1
        return res

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atMostKDistinct(A, K) - self.atMostKDistinct(A, K - 1)


A = [2, 1, 2, 1, 2]
K = 2
print(Solution().subarraysWithKDistinct(A, K))
