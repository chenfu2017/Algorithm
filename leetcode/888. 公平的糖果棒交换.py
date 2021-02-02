class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum1 = sum(A)
        sum2 = sum(B)
        total = (sum1 + sum2)>>1
        m1 = set(A)
        m2 = set(B)
        d = sum1 - total
        for i in m1:
            if i-d in m2:
                return [i,i-d]



A = [2]
B = [1,3]
print(Solution().fairCandySwap(A,B))