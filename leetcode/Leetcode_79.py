class Solution:
    visited = []

    d = [[0, 1], [-1, 0], [1, 0], [0, -1]]

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.visited.clear()
        l = [False] * len(board[0])
        for i in range(len(board)):
            self.visited.append(l.copy())
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.searchword(board, word, 0, i, j):
                    return True
        return False

    def searchword(self, board, word, index, x, y):
        if index == len(word) - 1:
            return board[x][y] == word[index]

        if board[x][y] == word[index]:
            self.visited[x][y] = True
            for i in self.d:
                newx = x + i[0]
                newy = y + i[1]
                # print('(%s,%s)' % (newx, newy))
                if newx >= 0 and newy >= 0 and newx < len(board) and newy < len(board[0]) \
                        and not self.visited[newx][newy] \
                        and self.searchword(board, word, index + 1, newx, newy):
                    return True
            self.visited[x][y] = False
        return False


board = [["A", "B", "C", "D", "E"],
         ["T", "S", "R", "Q", "F"],
         ["M", "N", "O", "P", "G"],
         ["L", "K", "J", "I", "H"]
    ]
word = "ABCDEFGHIJKLMNOPQRST"
print(Solution().exist(board, word))
