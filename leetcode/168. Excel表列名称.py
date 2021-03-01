class Solution:
    def convertToTitle(self, n: int) -> str:
        l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
        ans = ''
        while n > 0:
            n -= 1
            ans = l[n % 26] + ans
            n //= 26
        return ans


n = 28
print(Solution().convertToTitle(n))
