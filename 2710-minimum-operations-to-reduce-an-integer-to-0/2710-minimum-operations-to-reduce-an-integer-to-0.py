class Solution:
    def minOperations(self, n: int) -> int:
        
        ans = 0

        while n:
 
            if n&3 == 3:
                n += 1
                ans += 1
            elif n&1:
                n -= 1
                ans += 1                
            else:
                n >>= 1
        
        return ans

'''
    39 
    39 + 1 = 40 - 8 - 32 = 0

    39     (0010 0111)
    +1 : 40(0010 1000)
    40 // 8 = 5.(0101)
    -1 : 4 (0100) 

    1-0

    Power of 2
    0 1  2   3    4  5  6. 7.  8.  9.  10
    1 2  4   8    16 32 64 128 256 512 1024
bin 1 10 100 1000

    0x27
    0010 0111 -> 0010 1000
    add 1 subtract 1000, subtract 10

    simple examples
    11
        add 1 subtract 100
        subtract 1 subtract 10
    10
        subtract 10
    
    >> (right shift)
        no need to count because add or subtract



'''        