class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def f(upper):
            s = str(upper)
            @cache
            def dfs(i, val, diff, isLimit, isNum):
                if i == len(s):
                    return int(isNum and val == 0 and diff == 0)
                res = 0
                if not isNum: res = dfs(i+1, val, diff, False, False)
                bottom = 0 if isNum else 1
                top = int(s[i]) if isLimit else 9
                for d in range(bottom, top + 1):
                    res += dfs(i+1, (val * 10 + d) % k, diff + d % 2 * 2 - 1, isLimit and d == top, True)
                return res
            return dfs(0, 0, 0, True, False)
        return f(high) - f(low-1)
        

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

class Solution3:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        
        memo = [0,0,0]

        def countEvenOdd(n, evenCnt, oddCnt): 

            if n > high:
                return

            even_count = 0
            odd_count = 0

            if memo[0] != n:
                memo[0] = n
            while n: 
                if ((n % 10) % 2): 
                    memo[1] += 1
                else: 
                    memo[2] += 1

                n //= 10
            
            if even_count == odd_count:
                ans.append(num)
            
            
            countEvenOdd(n+k, )
            return (even_count == odd_count)

        num = low
        if low%k:
            num = low+(k - low%k)
        
        ans = []
        countEvenOdd(num)
        
        return len(ans)


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

    low digit count
        -> ex 1 1 4 7 4 8 3 6 4 7
                               +3
        -> ex 1 1 4 7 4 8 3 6 5 0 check k + 1 digit and update even/odd count  

        worse
              1 9 9 9 9 9 9 9 9 9                             
    hight digit count
    k digit count 
'''        