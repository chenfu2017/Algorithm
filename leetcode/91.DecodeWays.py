class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        m = [0] * (n + 1)
        m[0] = 1
        m[1] = 1
        for i in range(2, n + 1):
            if s[i - 1] != '0':
                m[i] = m[i - 1]
            if s[i - 2] == '1' or s[i - 2] == '2' and s[i - 1] <= '6':
                m[i] += m[i - 2]
        return m[n]


print(Solution().numDecodings("1226"))
