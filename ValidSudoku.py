'''
36. Valid Sudoku
Medium
9.1K
945
Companies
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

1 2 3 4 5 6 7 8 9
10 11 12 13 14 15 16 17 18
19 20 21 22 23 24 25 26 27

1. Brute Force

    1. Verify dup exists in Row lines
    2. Verify dup exists in Column lines
    3. Verify dup exists in 3x3 sub matrix

Runtime 115 ms Beats 70.87% Memory 16.5 MB Beats 14.40%

        COL_LEN = 9
        ROW_LEN = 9
        DELIMETER = '.'
        # 1. Verify row 9x1
        # 2. Verify col 1x9
        # 3. Verify 3x3

        #verification = [0] * [3][9]
        # 1st row : columns
        # 2nd row : rows
        # 3rd row : 3x3 from left to right, top to bottom
        
        veri_dict = defaultdict(str)
        
        for row in board:
            veri_dict.clear()
            for c in row:
                if c != DELIMETER and veri_dict.get(c):
                    return False
                else:
                    veri_dict[c] = 1

        for i in range(COL_LEN):
            veri_dict.clear()
            col = [val[i] for val in board]
            for c in col:
                if c != DELIMETER and veri_dict.get(c):
                    return False
                else:
                    veri_dict[c] = 1

        for i in range(0, ROW_LEN, 3):
            sub_3x3 = []
            for j in range(0, COL_LEN, 3):
                veri_dict.clear()
                for ii in range(3):
                    for jj in range(3):
                        c = board[i+ii][j+jj]
                        if c != DELIMETER and veri_dict.get(c):
                            return False
                        else:
                            veri_dict[c] = 1
        return True
'''


from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        COL_LEN = 9
        ROW_LEN = 9
        SUB_MAT = 3
        DELIMETER = '.'
        # 1. Verify row 9x1
        # 2. Verify col 1x9
        # 3. Verify 3x3

        #verification = [0] * [3][9]
        # 1st row : columns
        # 2nd row : rows
        # 3rd row : 3x3 from left to right, top to bottom
        
        veri_dict = defaultdict(str)
        
        for row in board:
            veri_dict.clear()
            for c in row:
                if c != DELIMETER and veri_dict.get(c):
                    return False
                else:
                    veri_dict[c] = 1

        for i in range(COL_LEN):
            veri_dict.clear()
            col = [val[i] for val in board]
            for c in col:
                if c != DELIMETER and veri_dict.get(c):
                    return False
                else:
                    veri_dict[c] = 1

        for i in range(0, ROW_LEN, SUB_MAT):
            sub_3x3 = []
            for j in range(0, COL_LEN, SUB_MAT):
                veri_dict.clear()
                for ii in range(SUB_MAT):
                    for jj in range(SUB_MAT):
                        c = board[i+ii][j+jj]
                        if c != DELIMETER and veri_dict.get(c):
                            return False
                        else:
                            veri_dict[c] = 1
        return True
                
            

s = Solution()
result = s.isValidSudoku(
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])

print(result)