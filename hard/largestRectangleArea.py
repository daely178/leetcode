'''
84. Largest Rectangle in Histogram
Hard
15.1K
215
Companies
Given an array of integers heights representing the histogram's bar height 
where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:

Input: heights = [2,4]
Output: 4
 
Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104

'''
import enum
from typing import List


class SolutionBruteForce():
    def largestRectangleArea(self, heights: List[int]) -> int:

        
        n = len(heights)
        left = [-1] * n
        right = [n] * n
        stack = []
        top = -1
        
        heights.append(0)

        for i in range(n):
            while stack and heights[stack[top]] >= heights[i]:
                stack.pop()
            # add first smaller value from left
            if stack:
                left[i] = stack[top]
            stack.append(i)
        stack = []
        for i in range(n, -1 ,-1):
            while stack and heights[stack[top]] >= heights[i]:
                stack.pop()
            # add first smaller value from right
            if stack:
                right[i] = stack[top]
            stack.append(i)

        maxarea = 0
        for i in range(n):
            maxarea = max(maxarea, (right[i]-left[i]-1)*heights[i])
            
        return maxarea
    
class SolutionStack():
    def largestRectangleArea(self, heights: List[int]) -> int:

        
        latest = -1
        maxarea = 0
        
        stack = [-1] # add -1 for leftmost boundary
        heights.append(0) # add 0 for additional iteration
        
        for right_boundary, curr_h in enumerate(heights):
            
            # look back heights and width
            while stack and heights[stack[latest]] > curr_h:
                
                latest_h = heights[stack.pop()]
                left_boundary = stack[latest]
                
                width = right_boundary - left_boundary - 1
                
                maxarea = max(maxarea, width*latest_h)
                
            stack.append(right_boundary)
            
        return maxarea
                

s = SolutionStack()
result = s.largestRectangleArea(heights = [2,1,5,6,2,3])

print(result)