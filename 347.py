'''
47. Top K Frequent Elements
Medium
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

heapq
Runtime 113 ms Beats 75.39% Memory 21.1 MB Beats 79.47%

        table = {}
        hq = []
        ans = []
        
        for num in nums:
            if table.get(num):
                table[num] += 1
            else:
                table[num] = 1
        for val, freq in table.items():
            heapq.heappush(hq, (-freq, val))
        
        heapq.heapify(hq)
            
        cnt = 0
        while cnt < k:
            item = heapq.heappop(hq)
            ans.append(item[1])
            cnt += 1
'''

from typing import List
from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        table = {}
        hq = []
        ans = []
        
        for num in nums:
            if table.get(num):
                table[num] += 1
            else:
                table[num] = 1
        for val, freq in table.items():
            heapq.heappush(hq, (-freq, val))
        
        heapq.heapify(hq)
            
        cnt = 0
        while cnt < k:
            item = heapq.heappop(hq)
            ans.append(item[1])
            cnt += 1
        return ans

s = Solution()
result = s.topKFrequent([1,1,1,2,2,3], 2)

print(result)