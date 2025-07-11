class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size() <= 1){
            return 0;
        }

        int buy = prices[0];
        int maxP = 0;
        for(int i=1; i<prices.size(); i++) {
            int sell = prices[i];

            if(sell > buy) {
                maxP = max(maxP, sell-buy);
            } else {
                buy = sell;
            }            
        }
        return maxP;
    }
};