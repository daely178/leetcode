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
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                if candidate < rooms[nr][nc]:
                    rooms[nr][nc] = candidate
                    heapq.heappush(hq, (candidate, nr,nc))
'''
    brute force
    dfs
        return distance

    
'''        