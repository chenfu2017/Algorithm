class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        l = [[0]*n for _ in range(n)]
        count = n*n
        i = 1
        state, x, y = [0] * 3
        while i <= count:
            l[x][y]=i
            r, c = d[state]
            if x + r >= n or x + r < 0 or y + c < 0 or y + c >= n or l[x + r][y + c]!=0:
                state = (state + 1) % 4
                r, c = d[state]
            x += r
            y += c
            i += 1
        return l

print(Solution().generateMatrix(2))
