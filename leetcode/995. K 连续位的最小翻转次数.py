from typing import List


class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        ans = 0
        n = len(A)
        diff = [0] * (n + 1)
        count = 0
        for i in range(n):
            count += diff[i]
            if (A[i] + count) %2 ==0:
                if i+K > n:
                    return -1
                ans +=1
                count +=1
                diff[i+K]-=1
        return ans
A = [0,0,0,1,0,1,1,0]
K = 3
print(Solution().minKBitFlips(A,K))