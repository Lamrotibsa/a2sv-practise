class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left_right , top_bottom = 0 ,len(matrix[0])
        right_left , bottom_top = len(matrix) , 0
        row , col = 0 , 0

        while left_right < right_left and top_bottom > bottom_top:

            while col < top_bottom:
                result.append(matrix[row][col])
                col += 1
            col -=1
            left_right +=1
            row = left_right
            while row < right_left:
                result.append(matrix[row][col])
                row +=1
            row-=1
            top_bottom -=1
            col = top_bottom
            if not(left_right < right_left and top_bottom > bottom_top):
                break
            while col > bottom_top:
                result.append(matrix[row][col-1])
                col -=1
            col+=1
            right_left -=1
            row = right_left-1
            
            while row >=left_right:
                result.append(matrix[row][col-1])
                row -= 1
            row+=1
            bottom_top +=1
            col = bottom_top
        return result


        
