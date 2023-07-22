'''
121. Best Time to Buy and Sell Stock
Easy
26.7K
853
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''


from typing import List
from collections import Counter

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
 
        # if len <= 1 return 0
        # set buy with prices[0]
        # compare prices[i] and set buy = prices[i] if buy < prices[i]
        # if prices[i] > buy, set profit = max( prev profit, prices[i] - buy )
        
        if len(prices) <= 0:
            return 0
        buy = prices[0]
        maxProfit = 0
        for sell in prices[1:]:
            
            if sell > buy:
                maxProfit = max(maxProfit, sell-buy)
            else:
                buy = sell
            
        return maxProfit
            

s = Solution()
result = s.maxProfit(prices = [7,1,5,3,6,4])

print(result)