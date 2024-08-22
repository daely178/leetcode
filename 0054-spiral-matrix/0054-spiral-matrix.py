class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        n = len(matrix)
        m = len(matrix[0])
        UP,DOWN,RIGHT,LEFT = 0,1,2,3
        ans = []
        visited = [[False for _ in range(m)] for _ in range(n)]

        def dfs(i,j, heading):

            visited[i][j] = True
            ans.append(matrix[i][j])

            # exit
            if heading == UP:
                if i-1 >= 0 and visited[i-1][j] == 0:
                    dfs(i-1, j, UP)
                elif j+1 <= m-1 and visited[i][j+1] == 0: # RIGHT
                    dfs(i, j+1, RIGHT)
                else:
                    return
            elif heading == RIGHT:
                if j+1 <= m-1 and visited[i][j+1] == 0:
                    dfs(i, j+1, RIGHT)
                elif i+1 <= n-1 and visited[i+1][j] == 0: # DOWN
                    dfs(i+1, j, DOWN)
                else:
                    return
            elif heading == DOWN:
                if i+1 <= n-1 and visited[i+1][j] == 0:
                    dfs(i+1, j, DOWN)
                elif j-1 >= 0 and visited[i][j-1] == 0: # LEFT
                    dfs(i, j-1, LEFT)
                else:
                    return
            elif heading == LEFT:
                if j-1 >= 0 and visited[i][j-1] == 0:
                    dfs(i, j-1, LEFT)
                elif i-1 >= 0 and visited[i-1][j] == 0: # UP
                    dfs(i-1, j, UP)
                else:
                    return


        dfs(0,0, RIGHT)

        return ans
'''
 1  2  3  4  5  6
 18 19          7
 17             8
 16             9
 15 14 13 12 11 10


'''                