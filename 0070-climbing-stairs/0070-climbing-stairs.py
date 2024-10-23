class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0]*(n+1)
        def helper(i, n):
            if i>n:
                return 0
            if i==n:
                return 1
            if memo[i]:
                return memo[i]
            memo[i] = helper(i+1, n) + helper(i+2,n)
            return memo[i]
            
        return helper(0, n)


'''
                0
        1               2
    1       2       1       2
1   2.    1.  2.  1.  2.  1   2
n=3
    0 0 0 0
'''        
        