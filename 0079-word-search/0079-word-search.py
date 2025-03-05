class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])

        def dfs(r,c, idx):
            if idx == len(word):
                return True            
            if r>=m or c >= n or r < 0 or c < 0 or board[r][c] != word[idx]:
                return False

            temp, board[r][c] = board[r][c], '/'
            res = dfs(r+1, c, idx+1) or dfs(r-1, c, idx+1) or dfs(r, c+1, idx+1) or dfs(r, c-1, idx+1)
            board[r][c] = temp

            return res

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if dfs(r,c,0) == True:
                        return True
        return False