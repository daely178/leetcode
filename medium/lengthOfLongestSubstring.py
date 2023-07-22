'''
3. Longest Substring Without Repeating Characters
Medium
35.4K
1.6K
Companies
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.


        left = 0
        substr = {}
        maxlen = 0
        for right in range(len(s)):
            if s[right] in substr:
                left = substr[s[right]] + 1
            else:
                maxlen = max(maxlen, right-left+1)
            substr[s[right]] = right
        return maxlen
'''

from typing import List
from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
 

        # iterate character and store in hash map
        # sliding window with left and right
        # increase right in loop
        # jump left to next to previous index when substr[ s[right] ] exists and 
        # index of current char in substr is bigger than left value
        # assign substr[ current char ] = right index value so that hash table gets updated with the latest index
        
        if len(s) <= 1:
            return len(s)
        
        left = 0
        substr = {}
        maxlen = 0
        for right in range(len(s)):
            if s[right] in substr and substr[s[right]] >= left:
                left = substr[s[right]] + 1
            else:
                maxlen = max(maxlen, right-left+1)
            substr[s[right]] = right
        return maxlen

s = Solution()
result = s.lengthOfLongestSubstring(s = "abcabcbb")

print(result)