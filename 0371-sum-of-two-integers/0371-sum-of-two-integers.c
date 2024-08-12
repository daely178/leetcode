int getSum(int a, int b) {

    unsigned int carry = 0;
    while (b&0xffffffff){
        carry = a&b;
        a = a^b;
        b = (unsigned int )(carry<<1);
    }

    return a;    
}