class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose():
            for i in range(len(matrix)):
                for j in range(i, len(matrix)):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        def swapColumns():
            length = len(matrix)
            for i in range(length):
                for j in range(length//2):
                    matrix[i][j], matrix[i][length-1-j]  = matrix[i][length-1-j], matrix[i][j]
        
        transpose()
        swapColumns()
        return
