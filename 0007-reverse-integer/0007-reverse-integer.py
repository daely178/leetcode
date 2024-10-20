class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x *= sign
        temp = 0
        while x:
            temp = temp*10 + x%10
            x //= 10
        
        temp *= sign

        if temp > 2**31-1 or temp < -2**31:
            return 0
        return temp
'''
    make positive

    

    [-2^31, 2^31 - 1]

    123
    1*10**2 + 2*10**1 + 3*10**0
    
    while x:
        temp = temp*10 + x%10
        x = x//10
    
    result > [-2^31, 2^31 - 1]
        return 0

'''        