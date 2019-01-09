class Solution:
    col = []
    diag1 = []
    diag2 = []
    res = []

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.col = [False] * n
        self.diag1 = [False] * (2 * n - 1)
        self.diag2 = [False] * (2 * n - 1)
        self.res.clear()
        row = []
        self.putQueen(n, 0, row)
        return self.res

    def getres(self, n, row):
        list = []
        for i in  range(n):
            str=''
            for j in range(n):
                if j==row[i]:
                    str+='Q'
                else:
                    str += '.'
            list.append(str)
        return list

    def putQueen(self, n, index, row):
        if index == n:
            self.res.append(self.getres(n,row))
            return

        for i in range(n):
            if not self.col[i] and not self.diag1[i + index] and not self.diag2[index - i + n - 1]:
                row.append(i)
                self.col[i] = True
                self.diag1[i + index] = True
                self.diag2[index - i + n - 1] = True
                self.putQueen(n, index + 1, row)
                self.col[i] = False
                self.diag1[i + index] = False
                self.diag2[index - i + n - 1] = False
                row.pop()
        return


print(Solution().solveNQueens(4))
