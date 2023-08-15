'''
287. Find the Duplicate Number
Medium
20.4K
3.3K
Companies
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
'''

from typing import List

class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:

        htable = {}

        for num in nums:
            if htable.get(num):
                return num
            htable[num] = 1
        return 0

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Use concept of 142. Linked List Cycle II (find the node where linked list has cycle)
        
        # start hopping from Node
        slow, fast = 0, 0
        # Cycle detection
        # Let slow jumper and fast jumper meet somewhere in the cycle 
        while True:
            # slow jumper hops 1 step, while fast jumper hops two steps forward.
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        # for locating start node of cycle
        check = 0
        while True:
            # Locate the start node of cycle (i.e., the duplicate number)
            slow = nums[slow]
            check = nums[check]
            
            if check == slow:
                break
        
        return check
    
s = Solution()
result = s.findDuplicate(nums = [1,9,2,4,7,5,3,9,8])

print(result)

# key points
# 1. nums array, len : n+1, range [1,n], 1<n<10 5exp
# 2. 1 <= nums[i] <= n
# 3. only one repeated number
# 4. return repeated number
# 5. Do not modify input array nums but use O(1) extra space

# Why linkedlist?
# 1. if integers 1 < nums[i]