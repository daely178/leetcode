class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
        


'''
 N 3

 0 0 0 0 0
dp[i] = dp[i-1] + dp[i-2]

            0
        1       2
    2       3 3
3
        
'''        
        