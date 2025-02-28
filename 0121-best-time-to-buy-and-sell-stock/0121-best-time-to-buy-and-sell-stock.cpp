class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = prices[0];
        int best = 0;
        
        for(int i=1; i<prices.size(); i++){
            int sell = prices[i];
            if(buy < sell)
                best = max(sell - buy, best);
            else
                buy = sell;
        }
        return best;
    }
};