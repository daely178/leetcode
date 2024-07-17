class Solution:
    def canPartition(self, nums: List[int]) -> bool:
                
        if sum(nums)&1:
            return False
        
        total = sum(nums)//2
        dp = [True]+[False]*(total+1)
        
        for num in nums:
            for curr in range(total, num-1, -1):
                dp[curr] = dp[curr] or dp[curr-num]
        return dp[total]

'''
    nums = [1,5,11,5]
    half_sum = 22/2 = 11

    1       0 1 2 3 4 5 6 7 8 9 10 11
        dp [T F F F F F F F F F  F F]
            T T F F F F F F F F  F F
                    F F F F F F  F F
        11~1
        dp[0] or dp[0]    

    brute force
    half_sum = sum//2 # 2 partitions sum is same as total sum
    
    nums = [1,5,11,5]
    half_sum = 22/2 = 11

    tree
                    11 : 1,5,11,5

                    select or not select current item

        5                        0
     16.      5           11           0
         10.    5        16.  11.   5.     0
        11 10. 6.  5              6.   5 1.   0

    11 : 1,5,11,5
dp
    0 1 2 3 4
  0 T F F F F
  1 F F F F F
  2 F F F F F
  3 F F F F F

'''        