class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        l = [i for i in range(1, n + 1)]
        p = []
        s = 1
        for i in range(1, n):
            s *= i
            p = [s] + p

        s = ''
        k = k - 1
        for i in range(n - 1):
            s = s + str(l.pop(k // p[i]))
            k = k % p[i]

        return s + [str(l[0]),'1'][s == '']

print(Solution().getPermutation(4,9))