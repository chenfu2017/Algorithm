from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            A[i].reverse()
            for j in range(len(A[i])):
                A[i][j] ^= 1
        return A



A=[[1,1,0],[1,0,1],[0,0,0]]
print(Solution().flipAndInvertImage(A))