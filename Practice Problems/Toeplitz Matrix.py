class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        dic = {}

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):

                diff = row - col
                if diff in dic:
                    if dic[diff] != matrix[row][col]:
                        return False
                else:
                    dic[diff] = matrix[row][col]

        return True


        
