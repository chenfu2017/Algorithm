class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix ==[]:
            return matrix
        l = []
        d= [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m,n=len(matrix),len(matrix[0])
        visited = [[False]* n for _ in range(m)]
        count = m * n
        i,state,x,y = [0]*4
        while i <count:
            l.append(matrix[x][y])
            visited[x][y] = True
            r, c = d[state]
            if x+r>=m or x+r<0 or y+c<0 or y+c>=n or visited[x+r][y+c]:
                state = (state + 1) % 4
                r, c = d[state]
            x += r
            y += c
            i += 1
        return l
l=[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print(Solution().spiralOrder(l))