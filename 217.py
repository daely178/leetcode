'''
217. Contains Duplicate
Easy

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

Brute force
Time limited exception
        for i in range(len(nums)):
            for j in range(i+1, len(nums), 1):
                if nums[i] == nums[j]:
                    return True
        return False
        
hash

Runtime 574 ms Beats 19.70% Memory 34.6 MB Beats 7.33%
        if len(nums) == 1:
            return False
        table = {}
        for num in nums:
            if table.get(num) != None:
                return True
            else:
                table[num] = 1
        return False
        
library
Runtime 563 ms Beats 31.10% Memory 30.8 MB Beats 72.31%
        if len(set(nums)) != len(nums):
            return True
        return False
'''

from typing import List
from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return False
        
        if set(nums) != nums:
            return True
        return False

s = Solution()
result = s.containsDuplicate([1,1,1,3,3,4,3,2,4,2])

print(result)