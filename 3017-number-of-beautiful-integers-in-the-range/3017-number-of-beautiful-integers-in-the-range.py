class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        
        @cache
        def dfs(s, index, odd, even, remainder, tight, leadingZero):
            if index >= len(s):
                return remainder % k == 0 and odd == even
            
            bound = int(s[index]) if tight else 9
            ans = 0
            for digit in range(bound + 1):
                add_odd = digit % 2 == 1
                add_even = digit % 2 == 0
                
                if leadingZero and digit == 0:
                    add_even = 0
                    
                ans += dfs(s, index + 1,
                           odd + add_odd,
                           even + add_even,
                           (remainder*10 + digit) % k,
                           tight and digit == int(s[index]),
                           leadingZero and digit == 0)
            return ans
        
        return dfs(str(high), 0, 0, 0, 0, True, True) - dfs(str(low - 1), 0, 0, 0, 0, True, True)
        
class SolutionBruteforce:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        
        def countEvenOdd(n): 

            even_count = 0
            odd_count = 0

            while n: 
                if ((n % 10) % 2): 
                    odd_count += 1
                else: 
                    even_count += 1
                    
                n //= 10
            
            return (even_count == odd_count)

        num = low
        if low%k:
            num = low+(k - low%k)
        
        ans = []
        while num <= high:  

            if countEvenOdd(num):
                ans.append(num)
            
            num += k
        
        return len(ans)

'''
    Input: low = 10, high = 20, k = 3

    num = low + (k-(low-(low//k)))
    ans

    while num <= high:

        ans.append(num)

        num += k

    return len(ans)

    1111 1111

    15

    -214 748 3648~ 2147483647

    max 10 digit


    DP
    f(n) = f(r)-f(l-1)
'''        