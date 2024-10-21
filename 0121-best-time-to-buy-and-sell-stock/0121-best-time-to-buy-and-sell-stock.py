class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        ans = 0
        buy = prices[0]
        for sell in prices[1:]:
            if buy > sell:
                buy=sell
            else:
                ans = max(ans, sell-buy)
        return ans
'''
    loop
    buy 
    sell
    profit = buy - sell
'''