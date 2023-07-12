'''
49. Group Anagrams
Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.


Runtime 119 ms Beats 55.90% Memory 20.2 MB Beats 60.14%
        ans = defaultdict(list)
        for str in strs:
            sorted_str = "".join(sorted(str))
            ans[sorted_str].append(str)
        
        return ans
'''

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)
        for str in strs:
            sorted_str = "".join(sorted(str))
            ans[sorted_str].append(str)
        
        return ans

s = Solution()
result = s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])

print(result)