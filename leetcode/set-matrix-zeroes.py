class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        cow = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row.add(i)
                    cow.add(j)
        
        
        for i in row:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0
        
        for j in cow:
            for i in range(len(matrix)):
                matrix[i][j] = 0