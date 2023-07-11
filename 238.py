from typing import List

'''
238. Product of Array Except Self
Medium
18.5K
1K
Companies
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        zero_cnt = 0
        zero_pos = 0
        product_all = 1

        # More than 2 zero : return all zero
        # 1 zero : Find zero position and put calculated value for zero position in result array
        # Non zero : divide product all by each num

        for id, val in enumerate(nums):
            if val == 0:
                zero_cnt += 1

                if zero_cnt > 1:
                    return [0]*len(nums)
                zero_pos = id
            else:
                product_all *= val

        if zero_cnt==1:
            ans[zero_pos] = product_all
            return ans
        
        for index in range(len(nums)):
            ans[index] = product_all//nums[index]

        return ans

s = Solution()
result = s.productExceptSelf([-1,1,0,-3,3])

print(result)
