class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix)==0:
            return
        row = []
        col = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row.append(i)
                    col.append(j)
        print(row)
        print(col)
        for i in row:
            for j in range(n):
                matrix[i][j]=0

        for i in range(m):
            for j in col:
                matrix[i][j]=0
        print(matrix)


n=[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Solution().setZeroes(n)