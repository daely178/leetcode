class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])
        zeros = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.append((i,j))
        
        for zero in zeros:
            matrix[zero[0]] = [0]*n
            for i in range(m):
                matrix[i][zero[1]] = 0
        