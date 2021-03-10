from typing import List


class Solution:
    def __init__(self):
        self.flag = False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = 9
        row = [[False] * n for _ in range(n)]
        col = [[False] * n for _ in range(n)]
        glid = [[False] * n for _ in range(n)]
        spaces = list()
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    index = ord(c) - ord('1')
                    row[i][index] = True
                    col[j][index] = True
                    box_index = (i // 3) * 3 + j // 3
                    glid[box_index][index] = True
                else:
                    spaces.append((i, j))

        def dfs(pos):
            if pos == len(spaces):
                self.flag = True
                return
            for c in range(9):
                i, j = spaces[pos]
                box_index = (i // 3) * 3 + j // 3
                if row[i][c] == col[j][c] == glid[box_index][c] == False:
                    row[i][c] = col[j][c] = glid[box_index][c] = True
                    board[i][j] = str(c+1)
                    dfs(pos + 1)
                    row[i][c] = col[j][c] = glid[box_index][c] = False
                if self.flag:
                    return
        dfs(0)
        # for i in range(9):
        #     print(board[i])

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(board)