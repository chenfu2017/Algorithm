class Solution:
    def titleToNumber(self, s: str) -> int:
        n = len(s)
        ans = 0
        n -= 1
        for c in s:
            ans += (ord(c) - 64) * 26 ** n
            n -= 1
        return ans


s = 'ZY'
print(Solution().titleToNumber(s))
