class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        ans = 0
        isprimer = [True] * n
        for i in range(2, n):
            if isprimer[i]:
                ans += 1
                for j in range(i * i, n, i):
                    isprimer[j] = False
        return ans


n = 10
print(Solution().countPrimes(n))
