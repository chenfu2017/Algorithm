class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        m = {}
        for i in range(len(C)):
            for j in range(len(D)):
                if C[i]+D[j] not in m:
                    m[C[i]+D[j]] = 0
                m[C[i]+D[j]]+=1
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if 0-A[i]-B[j] in m:
                    res += m[0-A[i]-B[j]]
        return res


