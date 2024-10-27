class Solution:
    def numIslands(self, grid):
        numIslands = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i,j):

            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j] != "1":
                return
            grid[i][j] = 'x'
            
            dfs(i+1, j)
            dfs(i,j+1)
            dfs(i-1, j)
            dfs(i, j-1)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    numIslands += 1
        
        return numIslands