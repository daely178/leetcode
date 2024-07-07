class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rq = deque()
        fresh_oranges = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rq.append((r,c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        minutes_elapsed = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while rq and fresh_oranges:
            rq_size = len(rq)    
            minutes_elapsed += 1
            for _ in range(rq_size):
                r,c = rq.popleft()
                for d in directions:
                    nr,nc = r+d[0], c+d[1]
                    if rows > nr >= 0 and cols > nc >= 0 and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        rq.append((nr, nc))

        return minutes_elapsed if fresh_oranges == 0 else -1

# [[2,1,1],
#. [1,1,0],
#. [0,1,1]]