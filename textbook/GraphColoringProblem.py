class Solution:
    def __init__(self):
        self.count = 0
        self.res = []

    def check(self, G, i, x):
        for k in range(len(G)):
            if G[i][k] and x[i] == x[k]:
                return False
        return True

    def find(self, G, m, i, x):
        n = len(G)
        if i == n:
            self.count += 1
            self.res.append(x.copy())
            return
        for c in range(m):
            x[i] = c
            if self.check(G, i, x):
                self.find(G, m, i + 1, x)
                x[i:] = [-1] * (n - i)


# G = [
#     [0, 1, 0, 0, 0, 0, 1],
#     [1, 0, 1, 1, 1, 1, 1],
#     [0, 1, 0, 1, 0, 0, 0],
#     [0, 1, 1, 0, 1, 0, 0],
#     [0, 1, 0, 1, 0, 1, 0],
#     [0, 1, 0, 0, 1, 0, 0],
#     [1, 1, 0, 0, 0, 1, 0]
# ]
G = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
]
s = Solution()
s.find(G, 3, 0, [-1] * len(G))
print(s.res)
print(s.count)
