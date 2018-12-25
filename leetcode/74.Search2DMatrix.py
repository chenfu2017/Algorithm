class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0 or len(matrix[0])==0 or target>matrix[-1][-1]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        l = []
        for i in range(m):
            l.append(matrix[i][0])
        i,j=0,m
        while i<=j and (i + j)//2<m:
            mid = (i + j)//2
            if target==l[mid]:
                return True
            elif target<l[mid]:
                j = mid-1
            else:
                i = mid+1
        if j ==-1:
            return False
        row = j
        i,j = 0,n
        while i<=j:
            mid = (i + j) // 2
            if target==matrix[row][mid]:
                return True
            elif target<matrix[row][mid]:
                j = mid-1
            else:
                i = mid+1
        return False
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print(Solution().searchMatrix([[]],3))