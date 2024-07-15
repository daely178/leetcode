class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @lru_cache(None)
        def dfs(remaining):
            if remaining < 0:
                return -1
            if remaining == 0:
                return 0
            min_cost = float('inf')
            for coin in coins:
                res = dfs(remaining-coin)
                if res != -1:
                    min_cost = min(min_cost, res+1)
            return min_cost if min_cost != float('inf') else -1
        return dfs(amount)
                    

'''
    brute force 
    deduct coin if coin <= amount
    amount - coin
    then next coin

    optimize
    coins = [1,2,5], amount = 11

                    11
          1           2           5
     1    2.   5. 1   2.   5.  1. 2.  5
 1 2 5    

    recursive for loop to choose all coins
'''