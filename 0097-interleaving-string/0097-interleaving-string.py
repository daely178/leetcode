
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [ [False]*(len(s2)+1) for _ in range(len(s1)+1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i<len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j<len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True                        

        return dp[0][0]

'''
    s1[i] == s3[i+j]
    s2[i] == s3[i+j]

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
    bottom up

        d b b c a
     a  F F F F F F
     a  F F F F F F
     b  F F F F F F
     c  F F F F F F
     c  F F F F F F i=4, j=4
        F F F F F T
'''


class Solution2:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Check if the combined length of s1 and s2 matches the length of s3
        if len(s1) + len(s2) != len(s3):
            return False
        
        # Initialize a dynamic programming array dp
        # dp[j] will store whether s1[0:i] and s2[0:j] can form s3[0:i+j]
        dp = [False] * (len(s2) + 1)
        
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    # Base case: Both s1 and s2 are empty, so s3 is also empty.
                    # Set dp[j] to True.
                    dp[j] = True
                elif i == 0:
                    # Base case: s1 is empty, so check if the previous dp[j-1]
                    # is True and if s2[j-1] matches s3[i+j-1].
                    dp[j] = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    # Base case: s2 is empty, so check if the current dp[j]
                    # is True and if s1[i-1] matches s3[i+j-1].
                    dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1]
                else:
                    # General case: Check if either the previous dp[j] or dp[j-1]
                    # is True and if the corresponding characters match s3[i+j-1].
                    dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])

        # Return the result stored in dp[len(s2)], which indicates whether
        # s1 and s2 can form s3 by interleaving characters.
        return dp[len(s2)]

'''
s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
i=2
j=1
i+j-1=2
s3    a a d b b c b c a c
s2        d b b c a
s1      a a b c c
  T F F F F F -101234
  T F F F F F   012345
  T 
i=2
j=1
(dp[j] and s1[i - 1] == s3[i + j - 1])=False
(dp[j - 1] and s2[j - 1] == s3[i + j - 1])=True
i+j-1=2
(dp[j] and s1[i - 1] == s3[i + j - 1])=False
(dp[j - 1] and s2[j - 1] == s3[i + j - 1])=True
i+j-1=3
(dp[j] and s1[i - 1] == s3[i + j - 1])=False
(dp[j - 1] and s2[j - 1] == s3[i + j - 1])=True
i+j-1=4
(dp[j] and s1[i - 1] == s3[i + j - 1])=False
(dp[j - 1] and s2[j - 1] == s3[i + j - 1])=True
i+j-1=5
(dp[j] and s1[i - 1] == s3[i + j - 1])=False
(dp[j - 1] and s2[j - 1] == s3[i + j - 1])=False  
'''        