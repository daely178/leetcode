class DetectSquares:

    def __init__(self):
        self.mypoints = Counter()

    def add(self, point: List[int]) -> None:
        self.mypoints[tuple(point)] += 1

    
    def count(self, point: List[int]) -> int:
        ans = 0
        x1,y1 = point
        for (x3,y3),cnt in self.mypoints.items():

            if y1-y3==0 or abs(x1-x3) != abs(y1-y3):
                continue
            ans += cnt*self.mypoints[(x1,y3)]*self.mypoints[(x3,y1)]
        
        return ans

'''
    x1,y1      x3,y3
    nx,ny      x4,y4

 diagonal
 vertial
 horizontal
'''