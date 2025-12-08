class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.empty()) {
            return 0;
        }
        int buy=prices[0];
        int profit=0;
        for(int i=1; i<prices.size(); i++) {
            int sell = prices[i];
            if(sell > buy) {
                profit = max(profit, sell-buy);
            } else {
                buy = sell;
            }            
        }
        return profit;
    }
};


/*

buy stock on ith day
sell stock on the different day in the future

find the max profit
cannot acheive 0 profit

buy = prices[0]
for loop
if sell > buy
    profit = max(sell - buy, profit)
    update profit until sell <= buy
else
    buy = sell


[7,1,5,3,6,4]
1=buy
4=sell
profit = 5

[7,6,4,3,1]
1=buy
1=sell


*/
