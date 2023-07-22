'''
567. Permutation in String
Medium
10.2K
327
Companies
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.


1. Brute Force
Timeout
        s3 = list(s1)
        window = len(s1)
        
        for i in range(len(s2)):
            substring = list(s2[i:i+window])
            matched = 0
            for j in range(window):
                if s3[j] in substring:
                    matched += 1
                    substring.remove(s3[j])
                else:
                    break
            if matched == window:
                return True
        return False
        
        for i in range(len(s2)):
            if s2[i] in cntr: 
                cntr[s2[i]] -= 1
                if cntr[s2[i]] == 0:
                    matched += 1
            if i >= w and s2[i-w] in cntr: 
                if cntr[s2[i-w]] == 0:
                    matched -= 1
                cntr[s2[i-w]] += 1

            if matched == len(cntr):
                return True        
        
        for i in range(len(s1)):
            if s2[i] in cntr: # decrease count by 1 whenever found
                cntr[s2[i]] -= 1
                if cntr[s2[i]] == 0: # count only once for current char
                    matched += 1

        for i in range(len(s1), len(s2), 1):
            if s2[i] in cntr: # decrease count by 1 whenever found
                cntr[s2[i]] -= 1
                if cntr[s2[i]] == 0: # count only once for current char
                    matched += 1            
            if s2[i-w] in cntr: 
                if cntr[s2[i-w]] == 0: # 
                    matched -= 1
                cntr[s2[i-w]] += 1 # recover count when it is 

            if matched == len(cntr):
                return True
'''


from typing import List
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        cntr, w, matched = Counter(s1), len(s1), 0   
        for i in range(len(s2)):
            
            # Consume
            if s2[i] in cntr: 
                cntr[s2[i]] -= 1
                if cntr[s2[i]] == 0:
                    matched += 1
            
            # Restore
            if i >= w and s2[i-w] in cntr: 
                if cntr[s2[i-w]] == 0:
                    matched -= 1
                cntr[s2[i-w]] += 1

            if matched == len(cntr):
                return True
        return False

s = Solution()
result = s.checkInclusion(s1 = "ab", s2 = "aaaba")

print(result)