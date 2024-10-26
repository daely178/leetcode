class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        l,r = 0, len(self.nums)
        mid = 0

        while l<r:
            mid = l+(r-l)//2
            if self.nums[mid] > num:
                r = mid
            else:
                l = mid+1
        self.nums.insert(l, num)

    def findMedian(self) -> float:
        m = len(self.nums)
        if m&1:
            return self.nums[m//2]
        else:
            return (self.nums[m//2]+self.nums[m//2-1])*0.5

'''
    median,,
    sorting
    even - -1,-2,-3
    even - 1,2
    heap
         -3
      -1    -2
'''        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()