class Solution:

    def numDecodings(self, s: str) -> int:

        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2, len(dp)):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[-1]
'''
    brute force
    1. recursive
        decode index + 1
        decode index + 2 if 0 < s[index:index+2] <= 26
        exit condition
        if s[index] == "0"
            error
        if index >= (len-1) : len-1 : index+1, len : 
            count 1
    2. dp
        dp[0], dp[1] = 1,1 if s[0] != '0'
        dp[i] = dp[i-1]
        dp[i] += dp[i-2] if 10 <= int(s[index:index+2]) <= 26

        11106
             
             1 1 1 0 6
        id 0 1 2 3 4 5
        dp 1 1 0 0 0 0 


1 <= s.length <= 100
s contains only digits and may contain leading zero(s).

                "11106"
        1 1106          11 106
    1 1 106  1 11 06.  11 1 06   11 10 6
   1 1 1 06   x             O       O
        x
'''