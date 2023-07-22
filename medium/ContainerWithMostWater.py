'''
11. Container With Most Water
Medium
25.1K
1.4K
Companies
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

two pointers

Runtime Details 698ms Beats 82.06%of users with Python3
Memory Details 29.28mb Beats 83.53%of users with Python3

    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        ii = 0
        jj = n -1
        ans = 0
        while ii<jj:
            new_area = min(height[ii], height[jj])*(jj-ii)
            if new_area > ans:
                ans = new_area
            if height[ii] > height[jj]:
                jj -= 1
            else:
                ii += 1
        return ans
'''

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        ii = 0
        jj = n -1
        ans = 0
        while ii<jj:
            new_area = min(height[ii], height[jj])*(jj-ii)
            if new_area > ans:
                ans = new_area
            if height[ii] > height[jj]:
                jj -= 1
            else:
                ii += 1
        return ans
        
s = Solution()
result = s.maxArea([1,8,6,2,5,4,8,3,7])

print(result)