class Solution:
    def getSum(self, index: int, value: int, n: int) -> int:
        count = 0
        
        # On index's left:
        # If value > index, there are index + 1 numbers in the arithmetic sequence:
        # [value - index, ..., value - 1, value].
        # Otherwise, there are value numbers in the arithmetic sequence:
        # [1, 2, ..., value - 1, value], plus a sequence of length (index - value + 1) of 1s. 
        if value > index:
            count += (value + value - index) * (index + 1) // 2
        else:
            count += (value + 1) * value // 2 + index - value + 1
        
        # On index's right:
        # If value >= n - index, there are n - index numbers in the arithmetic sequence:
        # [value, value - 1, ..., value - n + 1 + index].
        # Otherwise, there are value numbers in the arithmetic sequence:
        # [value, value - 1, ..., 1], plus a sequence of length (n - index - value) of 1s. 
        if value >= n - index:
            count += (value + value - n + 1 + index) * (n - index) // 2
        else:
            count += (value + 1) * value // 2 + n - index - value
        
        return count - value
    
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if self.getSum(index, mid, n) <= maxSum:
                left = mid
            else:
                right = mid - 1
        
        return left
'''
nums[index] = max
total sum <= maxsum
abs(nums[x] - nums[x+1]) <= 1

.... index ....

   .    <- index to be maximum
  ...
 .....
.......

   .    <- index to be maximum
  ...
 ........
............

.    <- index to be maximum
...
.....
.......

      .    <- index to be maximum
    ...
  .....
.......

nums index : n-index   ...   n-index -1 index  index+1    ...     index + n -1
nums value : x-index   x-2     x-1    x      x - 1     x -2 ....  

sum formula = last value*(first val + last val)/2

nums[index]
left sum of index = nums[index]
right sum of index = 



Input: n = 4, index = 2,  maxSum = 6
Output: 2

 1,2,2,1


'''        