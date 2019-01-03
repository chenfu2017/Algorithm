class Solution:
    def __init__(self):
        self.v = [6, 10, 12]
        self.w = [1, 2, 3]
        self.x = [0] * len(self.w)
        self.bestValue = 0

    def dp(self, c):
        n = len(self.w)
        m = [[0] * (c + 1) for _ in range(n)]
        for j in range(c + 1):
            m[0][j] = [0, self.v[0]][j >= self.w[0]]
        for i in range(1, n):
            for j in range(1, c + 1):
                if self.w[i] > j:
                    m[i][j] = m[i - 1][j]
                else:
                    m[i][j] = max(m[i - 1][j], m[i - 1][j - self.w[i]] + self.v[i])
        j = c
        for i in range(n - 1, -1, -1):
            if m[i][j] > m[i - 1][j] or not i and j:
                self.x[i] = 1
                j = j - self.w[i]
        self.bestValue = m[-1][-1]
        return m[-1][-1]

    def backtracking(self, c, i, cv, cw, cx):
        if i >= len(self.w):
            if self.bestValue < cv:
                self.bestValue = cv
                self.x = cx.copy()
            return
        if cw + self.w[i] <= c:
            cx[i] = 1
            self.backtracking(c, i + 1, cv + self.v[i], cw + self.w[i], cx)
        cx[i] = 0
        if sum(self.v[i+1:])+cv>self.bestValue:
            self.backtracking(c, i + 1, cv, cw, cx)

    # def  branchBounding(self):


solution = Solution()
# solution.dp(5)
solution.backtracking(5, 0, 0, 0, [0] * 3)
print(solution.bestValue)
print(solution.x)
