class Solution:
    col = []
    diag1 = []
    diag2 = []
    row=0
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.col = [False] * n
        self.diag1 = [False] * (2 * n - 1)
        self.diag2 = [False] * (2 * n - 1)
        self.row=0
        self.putQueen(n, 0)
        return self.row

    def putQueen(self, n, index):
        if index == n:
            self.row += 1
        for i in range(n):
            if not self.col[i] and not self.diag1[i + index] and not self.diag2[index - i + n - 1]:
                self.col[i] = True
                self.diag1[i + index] = True
                self.diag2[index - i + n - 1] = True
                self.putQueen(n, index + 1)
                self.col[i] = False
                self.diag1[i + index] = False
                self.diag2[index - i + n - 1] = False
        return


n = 8
print(Solution().totalNQueens(n))
