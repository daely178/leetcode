class Solution:
    def getSum(self, a: int, b: int) -> int:
    
        carry = 0
        mask = 0xffffffff
        while b & mask != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        
        # for overflow condition like
        # -1
        #  1
        return a&mask if b > mask else a
'''
    1's complement : ~x
    2's complement : ~x + 1
    positive to negative : ~x+1
    proof : x : 3, 011 + 100 + 1 = 1000

    addition
    x+y
    while y:
        x = x^y         011^010 = 001
        y = (x&y)<<1    010 << 1 = 100 -> 101

    subtraction
    while y:
        011 - 010
        b = (~x&y).  100&010 = 0
        x = x^y         011^010 = 001
        y = b<<1        0<<1
    
    while y:
        3+ -4
        011 - 100
        b = 100&100 = 1 -> 0
        x = 111 -> 1
        y = 10
        
'''        