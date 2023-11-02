class Solution:
    def climbStairs(self, n: int) -> int:

        memo = [0]*(n+1)

        def dfs(n, i):

            if i > n:
                return 0
            if i == n:
                return 1

            if memo[i] > 0:
                return memo[i]

            memo[i] = dfs(n, i+1) + dfs(n, i+2)

            return memo[i]
        
        return dfs(n, 0)


'''
    5
    1 1 1 1 1
   1 2
 1 2 1 2
1  1 1
1. 1
'''        
        