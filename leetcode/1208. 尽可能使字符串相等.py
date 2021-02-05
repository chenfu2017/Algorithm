class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        i = j = 0


s = "abcd"
t = "bcdf"
cost = 3
print(Solution().equalSubstring(s,t,cost))