'''
42. Trapping Rain Water
Hard
27.5K
380
Companies
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 Example 1:
 
 Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
'''

from typing import List
from collections import defaultdict
import heapq

class Solution:
    def trap(self, height: List[int]) -> int:

        # water : 0, elevation : non zero
        # cases of trapped water
        # 1. skip first zero
        # 2. Main idea
        #   2-1. Diff bigger than 0 and set left
        #   2-2. temp sum diffs between height until left index reaches right index
        #   2-3. distance bigger than 0 between non zero(index diff), set right
        #   2-4. add up temp sum into result sum
        #   2-5. set left right to left
        # 3. Repeat 2 until end of height array
        # 4. Error check
        #   4-1. if there is no 



s = Solution()
result = s.trap([4,2,0,3,2,5])

print(result)