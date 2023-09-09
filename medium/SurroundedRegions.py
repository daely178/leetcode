'''
130. Surrounded Regions
Medium
7.8K
1.6K
Companies
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
Example 2:

Input: board = [["X"]]
Output: [["X"]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
'''

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """        
        rows = len(board)
        cols = len(board[0])
        dir = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(board, r, c):
            if r > (rows-1) or r < 0 or c > (cols-1) or c < 0 or board[r][c] != "O":
                return
            
            board[r][c] = 'T'
            # check all directions
            for elem in dir:
                dfs(board, r+elem[0], c+elem[1])                
        
        # check left / right edges
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(board, r, 0)
            if board[r][cols-1] == 'O':
                dfs(board, r, cols-1)
                
        # check upmost / downmost edges
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(board, 0, c)
            if board[rows-1][c] == 'O':
                dfs(board, rows-1, c)

        # convert O to X and T to O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X' 


# Case #1
# X X X X X X
# X X O X X X
# X X X X X X
# X X X X X X

# Case #2
# X X O X X X
# X X X X X X
# X X X X X X
# X X X X X X

# Case #3
# X X O X X X
# X X O X X X
# X X X X X X
# X X X X X X

# ["X","X","X","X"],
# ["X","O","O","X"],
# ["X","X","O","X"],
# ["X","O","X","X"]]

s = Solution()

board = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]

s.solve(board)

print(board)
