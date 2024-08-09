class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[1] * n for _ in range(m)]

        for col in range(1, m):
            for row in range(1, n):
                d[col][row] = d[col - 1][row] + d[col][row - 1]

        return d[m - 1][n - 1]


'''
Input: m = 3, n = 2
Output: 3

          1 2
        0 1 1
      1 1 2 3
      2 1 3 6
      3 1 4 10 
'''        