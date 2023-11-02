class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2:
            return x
        
        l = 0
        r = x // 2

        while l <= r:
            mid = l+(r-l) // 2
            num = mid*mid
            if num > x:
                r = mid -1
            elif num < x:
                l = mid + 1
            else:
                return mid
        
        return r