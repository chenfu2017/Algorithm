class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for c in s:
            i = t.find(c)
            if i == -1:
                return False
            else:
                t = t[i + 1:]
        return True
s = "abc"
t = "ahbccb"
print(Solution().isSubsequence(s,t))