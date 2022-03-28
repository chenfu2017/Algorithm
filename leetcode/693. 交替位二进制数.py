class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n <= 1:
            return True
        cur = n & 1
        while n > 0:
            n = n >>1
            if cur == n & 1:
                return False
            cur = n & 1
        return True

print(Solution().hasAlternatingBits(4))

