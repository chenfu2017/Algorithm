from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        flag1 = True
        flag2 = True
        n = len(A)
        for i in range(1, n):
            if A[i] > A[i - 1]:
                flag1 = False
        for i in range(1, n):
            if A[i] < A[i - 1]:
                flag2 = False
        return flag1 or flag2
