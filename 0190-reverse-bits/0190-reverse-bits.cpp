class Solution {
public:
    int reverseBits(int n) {
        
       // signed integer
       // 1bit sign
       uint32_t nn = static_cast<uint32_t>(n);
       uint32_t reversed = 0;
       for(int i=0; i<32; i++) {
            if(n&1) {
                reversed |= (1<<(31-i));
            }
            n>>=1;
       }
       return static_cast<int>(reversed);
    }
};