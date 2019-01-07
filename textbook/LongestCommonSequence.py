class Solution:
    def lcs(self, m, n):
        len_n = len(n)+1
        len_m = len(m)+1
        c = [[0] * len_n for _ in range(len_m)]
        x = [[0] * len_n for _ in range(len_m)]
        for i in range(1, len_m):
            for j in range(1,len_n):
                if m[i - 1] == n[j - 1]:
                    c[i][j] = c[i - 1][j - 1] + 1
                    x[i][j] = 1
                elif c[i - 1][j] < c[i][j - 1]:
                    c[i][j] = c[i][j - 1]
                    x[i][j] = 2
                else:
                    c[i][j] = c[i - 1][j]
                    x[i][j] = 3
        self.show(len(m), len(n), m, x)
        print("为公共子序列，")
        return c[-1][-1]

    def show(self, i, j, m, x):
        if i == 0 or j == 0:
            return
        if x[i][j] == 1:
            self.show(i - 1, j - 1, m, x)
            print(m[i-1], end="  ")
        elif x[i][j] == 2:
            self.show(i, j - 1, m, x)
        else:
            self.show(i - 1, j, m, x)


m = [2, 3, 4, 5, 7, 8]
n = [3, 5, 6, 7, 9, 8]
print("长度为%d。"%Solution().lcs(m, n))
