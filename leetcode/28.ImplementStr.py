class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            return haystack.index(needle)
        except Exception:
             return -1


haystack = "aaab"
needle = "aaa"
print(Solution().strStr(haystack,needle))