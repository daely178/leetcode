'''
15. 3Sum
Medium
26.8K
2.4K
Companies
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

1. Using set()
def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        result = set()
        
        for i in range(N - 2):
            j = i + 1
            k = N - 1
            
            while i < j < k < N:
                num_sums = nums[i] + nums[j] + nums[k]
                if num_sums == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif num_sums < 0:
                    j += 1
                else:
                    k -= 1
        return list(result)
        
2. Using dictionary

3. Two pointers
'''

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        res = []
        
        for ii in range(n):
            
            # skip dup value
            if ii>0 and nums[ii-1] == nums[ii]: 
                continue
            
            jj = ii+1
            kk = n-1
            
            while jj<kk:
                
                sum = nums[ii] + nums[jj] + nums[kk]
                if sum == 0:
                    res.append([nums[ii], nums[jj], nums[kk]])
                    jj += 1
                    # skip dup value after adding incidence
                    while jj<kk and nums[jj-1] == nums[jj]:
                        jj += 1
                elif sum > 0:
                    kk -= 1
                elif sum < 0:
                    jj += 1
        return res
    
s = Solution()
result = s.threeSum([-1,0,1,2,-1,-4])

print(result)