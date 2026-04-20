class Solution {
public:
    int reverseBits(int n) {
        
        // 32 bits : 1bit sign, 31 bits : values

        int reversed = 0;
        for(int i=0; i<31; i++) {
            if(n&1) {
                reversed |= (1<<(31-i));
            }
            n>>=1;
        }

        return reversed;
    }
};