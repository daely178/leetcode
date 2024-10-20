class Solution:
    def numberToWords(self, num: int) -> str:
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven","Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["","Thousand", "Million", "Billion"]

        res = ""

        def helper(num):
            # xxx
            ans = ""
            if num == 0:
                return ""
            if num>=100:
                return ones[num//100] + " Hundred " + helper(num%100)
            elif num>=20:
                return tens[num//10] + " " + helper(num%10)
            else:
                return ones[num] + " "
        
        if num == 0:
            return "Zero"

        idx = 0
        while num:
            if num%1000:
                remainder = num%1000
                res = helper(remainder) + thousands[idx] + " " + res
            num = int(num/1000)
            idx += 1

        return res.strip()
'''
0 <= num <= 2^31 - 1 = 2,147,483,647

    Billion = 1,000,000,000
    Million = 1,000,000
    Thousand = 1,000
    Ten = 10
    1 = 1

    if num >= Billion:
        num = num / Billion
        ones[num / Billion] + "Billion"

    2,147,483 = 2,147,483,647 / 1000
    2,147 = 2,147,483 / 1000
    2 = 2,147 / 1000

    ex1)    647 = 6*100 + 4*10 + 7
    ex2)    617 = 6*100 + 17
    ex3) 10,617 = 10*1000 + 6*100 + 17

    num / 1000
     Six Hundred Seventeen
     Ten Thousand 

     10 


'''