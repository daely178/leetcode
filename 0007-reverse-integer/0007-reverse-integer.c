int reverse(int x){
    int sign = x>=0?1:-1;
    long result = 0;

    while(x){
        result = result*10 + x%10;
        x = (int)x/10;
    }

    if (result > INT_MAX || result < INT_MIN)
        return 0; 

    return (int)result;
}