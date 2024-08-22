class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rows = len(matrix)
        cols = len(matrix[0])
        ans = []
        left,right,up,down = 0, cols-1, 0, rows-1

        while len(ans)<rows*cols:
            for i in range(left, right+1):
                ans.append(matrix[up][i])
            up += 1
            for i in range(up, down+1):
                ans.append(matrix[i][right])
            right -= 1
            if up <= down:
                for i in range(right, left-1, -1):
                    ans.append(matrix[down][i])         
                down -= 1
            if left <= right:
                for i in range(down, up-1, -1):
                    ans.append(matrix[i][left])         
                left += 1                   

        return ans
'''
     0. 1. 2  3  4  5
    
0    1  2  3  4  5  6
1    18 19          7 
2    17             8
3    16             9
4    15 14 13 12 11 10


'''                