class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g,reverse=True)
        s = sorted(s,reverse=True)
        si = gi = res = 0
        while si < len(s) and gi < len(g):
            if s[si] >= g[gi]:
                res += 1
                si += 1
                gi += 1
            else:
                gi += 1

        return res

g = [2, 1, 3]
s = [1, 1]
print(Solution().findContentChildren(g, s))
