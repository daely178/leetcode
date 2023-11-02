class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        carry = 0
        alen = len(a)
        blen = len(b)
        ans = ""
        loopcnt = max(alen,blen)

        carry = 0
        i = 0
        while i<loopcnt:
            c = d = 0
            if alen-i-1>=0:
                c = int(a[alen-i-1])
            if blen-i-1>=0:
                d = int(b[blen-i-1])
            summ = c+d+carry
            if summ > 1:
                carry = 1
            else:
                carry = 0
            if summ == 2 or summ == 0:
                ans += "0"
            else:
                ans += "1"
            i += 1
        if carry:
            ans += "1"
        #print(ans)

        return ans[::-1]         

'''
       100
    110010

    110110
'''        

        