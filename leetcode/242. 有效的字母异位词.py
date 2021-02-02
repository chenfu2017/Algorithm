class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = [0] * 26
        n = [0] * 26
        for i in s:
            m[ord(i) - ord('a')] += 1
        for j in t:
            n[ord(j) - ord('a')] += 1
        for i in range(26):
            if m[i] != n[i]:
                return False
        return True


s = "a"
t = "ab"
print(Solution().isAnagram(s, t))
