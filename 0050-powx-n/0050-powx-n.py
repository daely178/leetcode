class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1

        if n < 0:
            n = n*-1
            x = 1/x

        powed = 1
        while n > 0:
            if n%2:
                powed *= x
                n -= 1
            x *= x
            n //= 2

        return powed


'''
    x=3, n=5

    3*3*3*3*3

    3*3 = 9 * 9 
'''        