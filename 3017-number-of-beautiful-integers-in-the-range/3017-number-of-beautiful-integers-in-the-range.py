class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        memo = {}
        digits = []
        
        def solve(pos, odd, even, rem, flag, lead_zero):
            if odd > len(digits) or even > len(digits):
                return 0
            if pos < 0:
                return int(odd == even and rem == 0)

            inputs = (pos, odd, even, rem, flag, lead_zero)
            if inputs in memo:
                return memo[inputs]

            answer = 0
            for digit in range(digits[pos] + 1 if flag else 10):
                new_odd = odd
                new_even = even
                if not lead_zero or digit > 0:
                    if digit % 2 == 1: 
                        new_odd += 1
                    else: 
                        new_even += 1
                new_rem = (rem * 10 + digit) % k
                new_flag = flag and (digit == digits[pos])
                new_lead_zero = lead_zero and (digit == 0)
                answer += solve(pos-1, new_odd, new_even, new_rem, new_flag, new_lead_zero)

            memo[inputs] = answer
            return answer

        def process(n):
            memo.clear()
            digits.clear()

            while n > 0:
                digits.append(n % 10)
                n //= 10

            return solve(len(digits)-1, 0, 0, 0, True, True)

        return process(high) - process(low-1)
        
        
class Solution2:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        
        @cache
        def dp(i, flag, rest, odd_even):
            if i == len(t):
                return flag >= 0 and not rest and not odd_even
            
            
            ans = int(0 < i < len(t) and not rest and not odd_even)
            for j in range(int(i == 0), 10):
                # compare the most significant digit with upper limit only when
                # previous comparsion are all equal (flag = 0)
                new_flag = flag
                if flag == 0:
                    # diff determined if current digit not equal with the one of upper limit
                    if j > int(t[i]): new_flag = -1
                    if j < int(t[i]): new_flag = 1
                    
                if j % 2:
                    ans += dp(i+1, new_flag, (rest * 10 + j) % k, odd_even+1)
                else:
                    ans += dp(i+1, new_flag, (rest * 10 + j) % k, odd_even-1)
            return ans
        
        t = str(high)
        h = dp(0, 0, 0, 0)
        dp.cache_clear()
        t = str(low - 1)
        l = dp(0, 0, 0, 0)
        return h - l

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