class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) < 1 or "" in strs:
            return ""

        first = strs[0]
        for i in range(len(first)):
            for str in strs[1:]:
                if i == len(str) or first[i] != str[i]:
                    return first[0:i]
                    
        return first

'''
    "flower",
    "flow",
    "flight"

    brute force

    1. find LCP between first two
    2. find LCP between #1 and 3rd

    Trie

    f
    l 
    o i g t
    w- word
    e
    r - word
'''        