class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        l = []
        for i in num:
            while l and l[-1] > i and k:
                k -=1
                l.pop()
            l.append(i)
        while k > 0:
            l.pop()
            k -= 1
        ans = ''
        isLeadingZero = True
        for i in l:
            if isLeadingZero and i == '0':
                continue
            else:
                isLeadingZero = False
                ans +=i
        return '0' if isLeadingZero else ans


num = "1432219"
k = 3
print(Solution().removeKdigits(num, k))
