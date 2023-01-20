class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        offset1 , offset2 = 0, 0
        for i in range(3):
            for j in range(3):
                sett1 = set()
                for row in range(offset1,offset1+3):
                    for col in range(offset2,offset2+3):
                        if board[row][col] in sett1 and board[row][col] !='.':
                            return False
                        sett1.add(board[row][col])
                
                offset1+=3
            offset1=0
            offset2+=3

        for row in range(len(board)):
            sett2 = set()
            for col in range(len(board[0])):
                if board[row][col] in sett2 and board[row][col] !='.':
                    return False
                sett2.add(board[row][col])
            

        for col in range(len(board[0])):
            sett3 = set()
            for row in range(len(board)):
                if board[row][col] in sett3 and board[row][col] !='.':
                    return False
                sett3.add(board[row][col])

        return True
        


