class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount+1, -1);
        dp[0] = 0;

        for(int i=1; i<=amount; i++) {
            for(int c : coins) {
                if(i-c>=0 && dp[i-c]!= -1){
                    dp[i] = dp[i]>0? min(dp[i], dp[i-c]+1) : dp[i-c]+1;
                }
            }
        }
        return dp[amount];
    }
};

/*
    coins = [1,2,5], amount = 11

    dp 0   1   2   3
       0  -1. -1. -1
                        7
                6       5         2
             5 4 1.  4  3 0.   1. 0 -3
        1 3 0 
            1. 2  5. 1.  2. 5  1  2  5


*/