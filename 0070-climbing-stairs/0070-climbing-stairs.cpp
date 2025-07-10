class Solution {
public:
    int climbStairs(int n) {
        if(n==1)
            return 1;
        std::vector<int> dp(n + 1); 
        dp[0] = 1;
        dp[1] = 1;
        for(int i=2; i<n+1; i++) {
            dp[i] = dp[i-1]+dp[i-2];
        }

        return dp[n];
    }
};

/*
    n = 2
    1 1
    2

    n = 3
            1            2 
        1.     2.    1     2
    1.     2 1
  1               1   
    4
     

    1 2 3 4 5
    1 2 3 5

    dp[i] = dp[i-1] + dp[i-2]

    1 2 3 4 5
    1 1 1*3 1*4
      1 1,2 2,2
            1,2,1
        2,1 2,1,1
            1,1,2
*/