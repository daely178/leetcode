class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        if n <= 1:
            return 0

        cool, sell, buy = 0,0,-math.inf

        for i in range(0,n):

            pre_buy = buy
            pre_cool = cool
            pre_sell = sell

            buy = max(pre_buy, pre_cool-prices[i])
            sell = max(pre_sell, pre_buy+prices[i])
            cool = max(pre_cool, pre_sell)
        
        return max(sell, cool)

'''
1. Must sell before buy again
2. After sell, must cooldown 
3. multiple times

4 Profit calculation
- buy = minus price
- sell = plus price
- cooldown = no change

Decision : previous state
sell     <- buy or cooldown      --> con'd #1
cooldown <- sell or cooldown     --> con'd #2
buy      <- cooldown             --> con'd #1

price              1    2    3    0    2
profit per action

sell               0    1
buy               -1    -1
cooldown.          0   0

                       0-2 or -1
'''
