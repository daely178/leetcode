class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size() < 1)
            return 0;

        int buy = prices[0];
        int profit = 0;
        for(int i=1; i<prices.size(); i++){
            int sell = prices[i];
            if(sell > buy) {
                profit = max(profit, sell - buy);
            }
            else {
                buy = sell;            
            }
        }
        return profit;
    }
};