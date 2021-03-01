class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n < 2:
            return 10 ** n
        ans = 10
        sum = 9
        temp = 9
        if n < 11:
            for i in range(2, n + 1):
                sum = sum * temp
                temp -= 1
                ans += sum
            return ans
        else:
            for i in range(2, 11):
                sum = sum * temp
                temp -= 1
                ans += sum
            return ans


n = 0
print(Solution().countNumbersWithUniqueDigits(n))
