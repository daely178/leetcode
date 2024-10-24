class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * (amount+1)
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i-coin>=0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] == amount + 1 else dp[amount]

'''
    [1,2,5], amount = 11
    1-10, 1-9

    select 1 - DFS
'''