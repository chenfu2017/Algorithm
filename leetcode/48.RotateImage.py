class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)-1
        if n > 0:
            for i in range((n+1) // 2):  # i is layer starting with 0
                for j in range(i, n - i):  # j iterates for layer i
                    matrix[i][n- j], matrix[n - j][n - i], matrix[n - i][j], matrix[j][i] = \
                    matrix[j][i], matrix[i][n- j], matrix[n - j][n - i], matrix[n - i][j]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
# matrix =[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
Solution().rotate(matrix)
