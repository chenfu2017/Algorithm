class Solution:

    m =[0,1,2,3]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return self.m[n]
        k = len(self.m)
        for i in range(k, n + 1):
            j, minval = 1, float('inf')
            while i - j * j >= 0:
                minval = min(minval, self.m[i - j * j] + 1)
                j += 1
            self.m.append(minval)
        return self.m[n]

print(Solution().numSquares(12))
