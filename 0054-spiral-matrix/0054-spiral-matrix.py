class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        n = len(matrix)
        m = len(matrix[0])
        ans = []
        UP = 1

        def dfs(i,j, heading):

            if i<n and i>=0 and j<m and j>=0 and matrix[i][j] != '$':
                ans.append(matrix[i][j])
                matrix[i][j] = '$'

                if j+1>=i:
                    dfs(i, j+1, UP)
                dfs(i+1,j,0)
                dfs(i,j-1,0)
                dfs(i-1,j,0)


        dfs(0,0, 0)

        return ans
'''
 1  2  3  4  5  6
 18 19          7
 17             8
 16             9
 15 14 13 12 11 10


'''                