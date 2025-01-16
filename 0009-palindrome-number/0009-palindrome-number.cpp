class Solution {
public:
    bool isPalindrome(int x) {
        int org = x;
        unsigned int reversed = 0;

        if (x<0)
            return false;

        while (x!=0){
            reversed = reversed*10 + (int)(x%10);
            x = (int)(x/10);
        }

        if (org != reversed) {
            return false;
        }
        return true;
    }
};