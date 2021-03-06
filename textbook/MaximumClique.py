class Solution:
    def __init__(self):
        self.x = []
        self.bestn = 0

    def check(self, G, i, cx):
        for j in range(i):
            if cx[j] and not G[i][j]:
                return False
        return True

    def find(self, i, G, cx, cn):
        n = len(G)
        if i == n:
            if cn > self.bestn:
                self.bestn = cn
                self.x = cx.copy()
            return
        cx[i] = 1
        if self.check(G, i, cx):
            self.find(i + 1, G, cx, cn + 1)
        if cn + n - i > self.bestn:
            cx[i] = 0
            self.find(i + 1, G, cx, cn)


G = [
    [0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0]
]
s = Solution()
s.find(0, G, [0] * len(G), 0)
print(s.x)
print(s.bestn)
