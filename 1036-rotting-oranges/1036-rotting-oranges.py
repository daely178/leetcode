class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        oranges = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    oranges += 1
        
        q.append((-1, -1))

        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while q:
            r,c = q.popleft()
            if r == -1:
                minutes_elapsed +=1
                if q:
                    q.append((-1,-1))
            else:
                for d in directions:
                    nr,nc = r+d[0], c+d[1]
                    if rows > nr >= 0 and cols > nc >= 0 and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        oranges -= 1
                        q.append((nr, nc))
        return minutes_elapsed if oranges == 0 else -1

# [[2,1,1],
#. [1,1,0],
#. [0,1,1]]