class DetectSquares2:

    def __init__(self):
        self.pointsCntr = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.pointsCntr[tuple(point)] += 1
        self.points.append(point)
    
    def count(self, point: List[int]) -> int:
        ans = 0
        x1,y1 = point
        for x3,y3 in self.points:
            if y1-y3==0 or x1-x3==0 or abs(x1-x3) != abs(y1-y3):
                continue
            ans += self.pointsCntr[(x1,y3)]*self.pointsCntr[(x3,y1)]
        
        return ans

class DetectSquares:
    def __init__(self):
        self.pointsCntr = Counter()

    def add(self, point: List[int]) -> None:
        self.pointsCntr[tuple(point)] += 1
    
    def count(self, point: List[int]) -> int:
        ans = 0
        x1,y1 = point
        for (x3,y3),cnt in self.pointsCntr.items():
            if y1-y3==0 or x1-x3==0 or abs(x1-x3) != abs(y1-y3):
                continue
            ans += cnt*self.pointsCntr[(x1,y3)]*self.pointsCntr[(x3,y1)]
        
        return ans
'''
    x1,y1      x3,y3
    nx,ny      x4,y4

 diagonal x1-x2 != 0 && y1-y2 !=0 -> x1-y2 == y1-x2 
 vertial. x1-x2 = 0 && y1-y2 != 0
 horizontal y1-y2 = 0 && x1-x2 != 0
'''