class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = {}
        l,r,longest = 0,0,0

        while r<len(s):
            if s[r] in seen:
                l = max(l, seen[s[r]]+1)
            longest = max(longest, r-l+1)
            seen[s[r]] = r
            r += 1
        return longest

'''
        a b c a b c b b
        l
          r
seen    0 1
longest 1 2
'''        