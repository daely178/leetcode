'''
167. Two Sum II - Input Array Is Sorted
Medium
10K
1.3K
Companies
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.

1. Brute force
Time limit exceeded 
        n = len(numbers)
        for i in range(n):
            for j in range(i+1, n, 1):
                if (numbers[i]+numbers[j]) == target:
                    return [numbers[i], numbers[j]]

2. search
Runtime 137 ms Beats 75.98% Memory] 17.2 MB Beats 61.36%

        i = 0
        j = len(numbers) -1
        
        while i<j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i + 1 , j + 1]
            
            if s > target:
                j-=1
            else:
               i+=1 
        
        return [i, j]

'''

from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers = [2,7,11,15], target = 9, [1,2]
        # numbers = [2,3,4], target = 6 [1,3]
        # numbers = [-1,0], target = -1 [1,2]
        # numbers = [0,0,3,4], target = 0 [1,2]
        
        # Target - val = the value to find
        # Find diff val
        #   1. no same value : dict[diff val]
        #   2. same value exists : 
        # Return ids
        
        # Data structure : [ [val, id, count], [val2, id2, count] .... ]
        
        i = 0
        j = len(numbers) -1
        
        while i<j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i + 1 , j + 1]
            
            if s > target:
                j-=1
            else:
               i+=1 
        
        return [i, j]

s = Solution()

#result = s.twoSum([12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997], 542)

result = s.twoSum([0,0,3,4], 0)
print(result)