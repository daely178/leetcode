from typing import List

'''
1. Two Sum
Easy
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

1. brute force
Runtime 3650 ms Beats 32.37% Memory 17 MB Beats 99.70%
       for i in range(len(nums)):
           for j in range(i+1, len(nums), 1):

               if (nums[i] + nums[j]) == target:
                   return [i,j]
                   
2. Hash

Runtime 87 ms Beats 44.13% Memory 17.6 MB Beats 54.38%

        table = {}
        for i in range(len(nums)):
            table[nums[i]] = i
            
        for i in range(len(nums)):
            if table.get(target-nums[i]):
                if table[target-nums[i]] != i:
                    return i, table[target-nums[i]]

        return [0,0]
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:




# hash
        table = {}
        for i in range(len(nums)):
            table[nums[i]] = i
            
        for i in range(len(nums)):
            if table.get(target-nums[i]):
                if table[target-nums[i]] != i:
                    return i, table[target-nums[i]]

        return [0,0]

s = Solution()
result = s.twoSum([1,3,4,2], 6)

print(result)
