class Solution:
    def romanToInt(self, s: str) -> int:

        if len(s) == 0:
            return 0

        RomanToInt = {
            'I':1,            
            'V':5,   #'IV':4,            
            'X':10,  #'IX':9,            
            'L':50,  #'XL':40,            
            'C':100, #'XC':90,            
            'D':500, #'CD':400,            
            'M':1000 #'CM':900,
        }

        i = 1
        total = 0
        total = prev = RomanToInt[s[0]]
        while i<len(s):

            curr = RomanToInt[s[i]]
            if prev == 1 and (curr == 5 or curr == 10):
                total += (curr - (prev<<1))
            elif prev == 10 and (curr == 50 or curr == 100):
                total += (curr - (prev<<1))
            elif prev == 100 and (curr == 500 or curr == 1000):
                total += (curr - (prev<<1))
            else:
                total += curr
            prev = curr

            # "MCMXCIV"
            #   M   C    M   X  C  I V
            # 1000 100 1000 10 100 1 5
            # V M
            # 5 1000

            i += 1
            
                
        return total