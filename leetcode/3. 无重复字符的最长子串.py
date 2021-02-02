class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        m = {}
        i = 0
        ans = 0
        for j in range(n):
            if s[j] in m:
                i = max(m[s[j]], i)
            ans = max(ans, j - i + 1)
            m[s[j]] = j + 1
        return ans


s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))
