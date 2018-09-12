class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        m = [-1] * (n + 1)
        m[1] = 1
        for i in  range(2,n+1):
            for j in range(1,i):
                m[i] = max(j*(i-j),m[i],j*m[i-j])
        return m[n]

print(Solution().integerBreak(10))

