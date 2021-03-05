class Solution:
    def findNthDigit(self, n: int) -> int:
        temp = 9
        num = 1
        count = 1
        while n > num * temp * count:
            n -= num * temp * count
            num *=10
            count +=1
        target = 10 ** (count-1) + (n-1)//count
        return str(target)[(n-1)%count]

n = 100
print(Solution().findNthDigit(n))