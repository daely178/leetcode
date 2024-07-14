class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        res = 0
        
        for i in range(n):

            # odd
            l, r = i, i
            while r<n and l>=0 and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            # even
            l, r = i, i+1
            while r<n and l>=0 and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res
'''
    brute force

    1. loop with char
    2. check left, right of c
    3. odd
        aa : c and c +1
    4. even
        abc : left c right

'''