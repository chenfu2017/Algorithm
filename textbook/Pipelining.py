class Solution:
    def __init__(self):
        self.bestf = float('inf')
        self.bestx = []

    def dowork(self, f, s, i, f1, f2, x):
        n = len(f)
        if i == n:
            if f2 < self.bestf:
                self.bestf = f2
                self.bestx = x.copy()
            return
        for j in range(i, n):
            f1 += f[x[j]]
            if max(f2, f1) + s[x[i]] < self.bestf:
                x[i], x[j] = x[j], x[i]
                self.dowork(f, s, i + 1, f1, max(f2, f1) + s[x[i]], x)
                x[i], x[j] = x[j], x[i]
            f1 -= f[x[j]]


f = [5, 12, 4, 8]
s = [6, 2, 14, 7]
n = len(f)
x = [i for i in range(n)]
solution = Solution()
solution.dowork(f, s, 0, 0, 0, x)
print(solution.bestx)
print(solution.bestf)
