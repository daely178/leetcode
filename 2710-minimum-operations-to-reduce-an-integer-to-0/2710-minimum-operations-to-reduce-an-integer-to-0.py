class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0

        while n:
            if n&3 == 3: # 3= bin(11)
                ans += 1
                n += 1

            elif n&1:
                ans += 1
                n -= 1

            else:
                n = n >> 1

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

    39
    0x27
    0010 0111 -> 0010 1000
    add 1 subtract 1000, subtract 10

    simple examples

    1111 (15)
    1 0000 -> -16

    11(3)
        add 1 subtract 100 (2^2)
        subtract 1 subtract 10 (2)
    10
        subtract 10
    
    >> (right shift)
        / 2
        1000
         100
           1
        32
        10000
        1-1
        no need to count because add or subtract

    
    39
    0x27
    0010 0111

    continuous 1 (두자리만)
        +1
        count +=1
        0010 1

    shift 3 번
        0000 0101

        -1
        count += 1
        0000 0100

        1
        -1
        count += 1
'''        