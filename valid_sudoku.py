'''
Valid Sudoku
Solution
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
'''

class Solution(object):
    def check_rows(self, board):
        for row in board:
            found = [False] * 9
            for col in row:
                if col == ".":
                    continue;
                n = ord(col) - ord("1")
                if found[n]:
                    return False
                found[n] = True
        return True
    
    def check_columns(self, board):
        for col in range(9):
            found = [False] * 9
            for row in range(9):
                v = board[row][col]
                if v == ".":
                    continue;
                n = ord(v) - ord("1")
                if found[n]:
                    return False
                found[n] = True
        return True
    
    # b - 0 1 2 3 ....8
    def check_box(self, board, b):
        bi = b/3
        bj = b%3
        col_start = 3*bj
        row_start = 3*bi
        found = [False] * 9
        for i in range(row_start, row_start+3):
            for j in range(col_start, col_start+3):
                v = board[i][j]
                if v == ".":
                    continue;
                n = ord(v) - ord("1")
                if found[n]:
                    return False
                found[n] = True
        return True
    def check_boxes(self, board):
        for i in range(9):
            if not self.check_box(board, i):
                print("BOX", i, "INVALID")
                return False
            else:
                print("BOX", i, "TRUE")
        return True
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        B = self.check_boxes(board)
        C = self.check_columns(board)
        R = self.check_rows(board)
        print("B:", B, "C:", C, "R:", R)
        return B and C and R

