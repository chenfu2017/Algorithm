from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        if not matrix or not matrix[0]:
            m, n = 0, 0
        else:
            m, n = len(matrix), len(matrix[0])
        for i in range(1, n):
            self.matrix[0][i] += self.matrix[0][i - 1]
        for i in range(1, m):
            self.matrix[i][0] += self.matrix[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                self.matrix[i][j] += self.matrix[i - 1][j] + self.matrix[i][j - 1] - self.matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.matrix[row2][col2]
        elif row1 == 0:
            return self.matrix[row2][col2] - self.matrix[row2][col1 - 1]
        elif col1 == 0:
            return self.matrix[row2][col2] - self.matrix[row1 - 1][col2]
        else:
            return self.matrix[row2][col2] - self.matrix[row2][col1 - 1] - self.matrix[row1 - 1][col2] + \
                   self.matrix[row1 - 1][col1 - 1]


# Your NumMatrix object will be instantiated and called as such:
matrix = [[-4,-5]]
obj = NumMatrix(matrix)
print(obj.sumRegion(0,0,0,1))

