'''
239. Sliding Window Maximum
Hard
15.1K
495
Companies
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

1. Brute force

Timeout
        ans = []
        
        for i in range(0, len(nums)-k+1, 1):
            subnums = nums[i:i+k]
            maxVal = -9999999
            
            for num in subnums:
                if num > maxVal:
                    maxVal = num
            ans.append(maxVal)
        
        return ans
        
2. Heap
        h,ans  =[],[]
        for i in range(k):heapq.heappush(h,(-nums[i],i))
        ans.append(-h[0][0])
        for i in range(k,len(nums)):
            heapq.heappush(h, (-nums[i],i))    
            while h and (i - h[0][1]) >=k:heapq.heappop(h)    
            ans.append((-h[0][0]))
        return ans
        
3. dequeue

        # create a deque to hold the indices of the elements in the sliding window
        window = deque()
        result = []
        
        # iterate through the array
        for i in range(len(nums)):
            # remove elements from the deque that are outside the window
            while window and window[0] <= i - k:
                window.popleft()
            
            # remove elements from the deque that are smaller than the current element
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            
            # add the index of the current element to the deque
            window.append(i)
            
            # add the maximum element in the window to the result list
            if i >= k - 1:
                result.append(nums[window[0]])
        
        return result
        
        h,ans  =[],[]
        for i in range(k):
            heapq.heappush(h,(-nums[i],i))
        ans.append(-h[0][0])
        for i in range(k,len(nums)):
            heapq.heappush(h, (-nums[i],i))    
            while h and (i - h[0][1]) >=k:heapq.heappop(h)    
            ans.append((-h[0][0]))
        return ans        
        
        window = deque()
        result = []
        
        # iterate through the array
        for i in range(len(nums)):
            # remove elements from the deque that are outside the window
            while window and window[0] <= i - k:
                window.popleft()
            
            # remove elements from the deque that are smaller than the current element
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            
            # add the index of the current element to the deque
            window.append(i)
            
            # add the maximum element in the window to the result list
            if i >= k - 1:
                result.append(nums[window[0]])
        
'''


from typing import List
from collections import deque
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q, res = deque(), []
        
        for r in range(len(nums)):
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()
                
            q.append(r)
            
            if r+1 < k: continue
            
            if r+1-k > q[0]:
                q.popleft()
            
            res.append(nums[q[0]])

        return res

s = Solution()
result = s.maxSlidingWindow(nums=[1,-1], k=1)

print(result)