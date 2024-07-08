class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return []

        rows = len(rooms)
        cols = len(rooms[0])

        hq = []
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    hq.append((0,r,c))
        
        while hq:
            distance, r, c = heapq.heappop(hq)
            candidate = distance + 1
            for nr, nc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr = nr + r
                nc = nc + c
                if rows > nr >= 0 and cols > nc >= 0:
                    if candidate < rooms[nr][nc]:
                        rooms[nr][nc] = candidate
                        heapq.heappush(hq, (candidate, nr,nc))
'''
    1 append gates to queue
    2 bfs from gate to inf positions to calculate distance from each gate
    3 do not visit

Q = 
    [  0, -1,  0,INF],
    [INF,INF,INF, -1],
    [INF, -1,INF, -1],
    [0,   -1,INF,INF]]
    
    [. 3, -1,  0,  1],
    [  2,  2,  1, -1],
    [. 1, -1,  2, -1],
    [0,   -1,  3,  4]]    
'''        