'''
128. Longest Consecutive Sequence
Medium
16.9K
726
Companies
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

hash and heapq
heappush : O(logn)
heappop : O(logn)
Time Complexity: O(nlogn) O(nlogn)
Space Complexity: O(n2)
Runtime 583 ms Beats 48.49% Memory 34 MB Beats 12.56%

        table = {}
        hq = []
        
        if len(nums) <= 1:
            return len(nums)
        
        for id, num in enumerate(nums):
            
            if table.get(num):
                table[num] += 1
            else:
                table[num] = 1
                heapq.heappush(hq, num)
        
        consec_cnt=1
        last_val = heapq.heappop(hq)
        largest_consec = 1
        while hq:
            curr_val = heapq.heappop(hq)
            if abs(last_val-curr_val) == 1:
                consec_cnt += 1
                if consec_cnt > largest_consec:
                    largest_consec = consec_cnt
            else:
                if consec_cnt > largest_consec:
                    largest_consec = consec_cnt
                consec_cnt = 1
            last_val = curr_val
        return largest_consec

'''
from typing import List
from collections import defaultdict
import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        table = {}
        hq = []
        
        if len(nums) <= 1:
            return len(nums)
        
        for id, num in enumerate(nums):
            
            if table.get(num):
                table[num] += 1
            else:
                table[num] = 1
                heapq.heappush(hq, num)
        
        consec_cnt=1
        last_val = heapq.heappop(hq)
        largest_consec = 1
        while hq:
            curr_val = heapq.heappop(hq)
            if abs(last_val-curr_val) == 1:
                consec_cnt += 1
                if consec_cnt > largest_consec:
                    largest_consec = consec_cnt
            else:
                if consec_cnt > largest_consec:
                    largest_consec = consec_cnt
                consec_cnt = 1
            last_val = curr_val
        return largest_consec
        
s = Solution()
result = s.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6])

print(result)