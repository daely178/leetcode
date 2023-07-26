'''
20. Valid Parentheses
Easy
20.9K
1.3K
Companies
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

from typing import List
from collections import deque
import heapq

class Solution:
    def isValid(self, s: str) -> bool:

        p, q, r = 0, 0, 0
        for c in s:
            if c == '(':
                p += 1
            elif c == ')':
                p -= 1
            elif c == '{':
                q += 1
            elif c == '}':
                q -= 1
            elif c == '[':
                r += 1
            elif c == ']':
                r -= 1
        if p == 0 and q == 0 and r == 0:
            return True
        return False

s = Solution()
result = s.isValid( s = "([)]")

print(result)
