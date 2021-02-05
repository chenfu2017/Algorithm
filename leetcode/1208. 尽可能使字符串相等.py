class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        n = len(s)
        left = right = 0
        res = 0
        while right < n:
            maxCost -= abs(ord(t[right]) - ord(s[right]))
            if maxCost >= 0:
                res = max(res, right - left + 1)
            else:
                maxCost += abs(ord(t[left]) - ord(s[left]))
                left += 1
            right += 1
        return res

s = "krrgw"
t = "zjxss"
cost = 19
print(Solution().equalSubstring(s, t, cost))
