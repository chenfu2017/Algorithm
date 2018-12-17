class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '#' + '#'.join(s) + '#'
        n = len(s)
        p = n * [0]
        maxx = id = index = 0
        for i in range(len(s)):
            if maxx > i:
                p[i] = min(maxx - i, p[2 * id - i])
            else:
                p[i] = 1
            while (i + p[i] < len(s) and i - p[i] >= 0 and s[i + p[i]] == s[i - p[i]]):
                p[i] += 1
            if i + p[i] > maxx:
                maxx = i + p[i]
                id = i
            if p[index] < p[i]:
                index = i
        l = ''
        for i in range(index - p[index] + 2, index + p[index] - 1):
            if s[i] == '#':
                continue
            l += s[i]
        return l


print(Solution().longestPalindrome("asa"))
