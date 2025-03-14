class Solution {
public:
    double myPow(double x, int n) {
        if(n==0)
            return 1;

        long nn = n;
        if(nn<0){
            nn *= -1;
            x = 1/x;
        }
        double result = 1;
        while(nn) {
            if(nn%2) {
                result *= x;
                nn--;
            }

            x *= x;
            nn /= 2;
        }
        return result;
    }
};