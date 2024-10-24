class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if text1 == text2:
            return len(text1)

        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]: 
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        
        return dp[len(text1)][len(text2)]
'''
text1 = "abcde", text2 = "ace" 

brute force
2 loops
abcde
a c e 



dp 0 1 2 3 4
   
      a b c d e
    0 0 0 0 0 0
  a 0 1 1 1 1 1
  c 0 1 1 2 2 2
  e 0 1 1 2 2 3

'''