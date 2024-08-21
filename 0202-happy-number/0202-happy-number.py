class Solution:

    

    def isHappy(self, n: int) -> bool:
        
        s = 0
        seen = set()

        while n!=1 and s not in seen:
            seen.add(s)
            s = 0
            while n>0:
                d = n%10
                n = int(n//10)
                s += d*d
            n = s

        return n==1

'''
    happy condition
    starting with positive - replace sum of squares of digits
    repeat until the number equals 1

    19 - 82 - 68 - 100 - 1
    2 - 4 - 8 - 16 - 37 - 37
'''        