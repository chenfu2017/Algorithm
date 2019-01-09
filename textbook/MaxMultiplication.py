class Solution:

    def kmltiplication(self, num, k):
        n = len(num)
        c = [[0] * n for _ in range(n)]
        m = [[0] * k for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                c[i][j] = int(num[i:j + 1])
        for i in range(n):
            m[i][0] = c[0][i]
        for i in range(1, n):
            for j in range(1, k):
                for d in range(i):
                    m[i][j] = max(m[i][j], m[d][j - 1] * c[d + 1][i])
        for i in c:
            for j in i:
                print("%8d" % j, end=' ')
            print()
        return m[-1][-1]


num = "14235"
print(Solution().kmltiplication(num, 3))
