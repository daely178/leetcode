class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        maxlen = 0

        for i in range(len(s)):

            # odd
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > maxlen:
                    maxlen = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1
        
            # even
            l, r = i, i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > maxlen:
                    maxlen = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1

        return res



# memoization
# recursive - re-use
# controlled brute force
# sub problem

# single ch
# odd : left - center ch - right

# even : left == right

# 'aaa'
#  'aa'
# 'ac'
# 'aba'