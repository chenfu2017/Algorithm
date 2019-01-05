class Solution:
    def inverted(self, num, l):
        if num > 0:
            l.append(num % 10)
            self.inverted(num // 10, l)


l = []
Solution().inverted(12345, l)
print(l)
