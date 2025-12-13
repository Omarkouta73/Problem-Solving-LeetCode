import numpy as np

class Solution:
    def isValidSudoku(self, board) -> bool:

        # Each row must contain the digits 1-9 without duplicates.
        for row in board:
            # no duplicates
            for i in range(len(row)):
                if row[i] == '.':
                    continue
                if row.count(row[i]) > 1:
                    return False
            
        # Each column must contain the digits 1-9 without duplicates.
        for row in range(9):
            # no duplicates
            seen = set()
            for col in range(9):
                if board[col][row] == '.':
                    continue
                if board[col][row] in seen:
                    return False
                seen.add(board[col][row])

        # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3)*3+i
                    col = (square%3)*3+j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

            
        return True
            
        

board = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]
sol = Solution()
print(sol.isValidSudoku(board))
