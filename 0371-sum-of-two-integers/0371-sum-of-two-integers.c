int getSum(int a, int b) {

    unsigned int carry = 0;
    while (b&0xffffffff){
        carry = a&b;
        a = a^b;
        b = carry<<1;
    }

    if (b>0)
        return a&0xffffffff;
    else
        return a;        
}