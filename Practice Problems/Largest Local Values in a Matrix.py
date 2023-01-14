class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = [[0 for j in range(len(grid[0])-2)] for i in range(len(grid)-2)]
        
        for row in range(len(result)):
            for col in range(len(result[0])):
                maxx = 0
                for i in range(row ,row+3):
                    for j in range(col , col+3):
                        maxx = max(maxx , grid[i][j])

                result[row][col] = maxx

        return result

        
        
        
        
    
