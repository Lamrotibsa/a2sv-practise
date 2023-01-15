class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        val = []
        i =[]
        j =[]
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    i.append(row)
                    j.append(col)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in i or col in j:
                    matrix[row][col] = 0

        
