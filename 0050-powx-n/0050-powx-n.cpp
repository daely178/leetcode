class Solution {
public:
    double myPow(double x, int n) {
        double res = 1;
        long nn = n;
        if(n<0){
            x = 1.0/x;
            nn *= -1;
        }

        while(nn) {
            if(nn%2){
                res = res*x;
                nn -= 1;
            }
            x *= x;
            nn >>= 1;
        }
        return res;
    }

        /*
            x^n
            2^-1 = 1/2
            2^-5 = 1/2^5
        */
};