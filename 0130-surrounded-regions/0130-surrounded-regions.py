class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        cols = len(board[0])

        def dfs(board, r, c):
            if r>(rows-1) or r < 0 or c <0 or c > (cols-1) or board[r][c] != 'O':
                return
            
            board[r][c] = 'T'

            dfs(board, r+1, c)
            dfs(board, r-1, c)
            dfs(board, r, c+1)
            dfs(board, r, c-1)

        # check 1 left/right

        for r in range(rows):
            if board[r][0] =='O':
                dfs(board, r, 0)
            if board[r][cols-1] == 'O':
                dfs(board, r, cols-1)

        # check 2 up / down
        for c in range(cols):
            if board[0][c] =='O':
                dfs(board, 0, c)
            if board[rows-1][c] == 'O':
                dfs(board, rows-1, c)

        # final step
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
