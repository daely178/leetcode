class Solution {
public:
    int climbStairs(int n) {
        int stairs[n+1];

        stairs[0] = 1;
        stairs[1] = 1;

        for(int i=2; i<=n; i++) {
            stairs[i] = stairs[i-1] + stairs[i-2];
        }
        return stairs[n];
    }
};

/*
n
       1          2
    1     2    1.     2
 1.   2. 1. 2 1  2. 1.  2

 stairs[n+1] = {0,}
 stairs[0] = 1
 stairs[1] = 1
 stairs[2] = 2
 stairs[3] = 3

 stair[n] = stairs[n-1] + stairs[n-2]
*/