from typing import List
from collections import Counter

'''
242. Valid Anagram
Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

1. Brute force
# Runtime 84 ms Beats 8.96% Memory 16.8 MB Beats 91.4%
        stable = {}
        ttable = {}
        if len(s) != len(t):
            return False
            
        for c in s:
            if stable.get(c) == None:
                stable[c] = 1
            else:
                stable[c] += 1
        for c in t:
            if stable.get(c) == None:
                return False
            else:
                if ttable.get(c) == None:
                    ttable[c] = 1
                else:
                    ttable[c] += 1
                    if ttable[c] > stable[c]:
                        return False
        return True 

2. Hash
Beats 43.18% Memory 16.9 MB Beats 63.90%
        stable = {}
        ttable = {}
        if len(s) != len(t):
            return False

        for id in range(len(t)):
            if stable.get(s[id]) == None:
                stable[s[id]] = 1
            else:
                stable[s[id]] += 1
            if ttable.get(t[id]) == None:
                ttable[t[id]] = 1
            else:
                ttable[t[id]] += 1

        if stable != ttable:
            return False
        return True

3. Libraries
Runtime 66 ms Beats 63.85% Memory 17.6 MB Beats 8.20%
return sorted(s) == sorted(t)

Runtime 56 ms Beats 89.17% Memory 17 MB Beats 36.99%
return Counter(s) == Counter(t)
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return Counter(s) == Counter(t)

s = Solution()
result = s.isAnagram("aacc", "ccac")

print(result)
