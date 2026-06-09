# 36. Valid Sudoku

#we can use hash maps to check if the numbers in each row, column and 3x3 box are unique. We can iterate through the board and for each number, we can check if it has already been seen in the current row, column or box. If it has, then the board is not valid. If it hasn't, we can add it to the corresponding hash map. If we finish iterating through the board without finding any duplicates, then the board is valid.


class Solution(object):
    def isValidSudoku(self, board):
        
       

        for row in board:
            checked= set()    #need to check each row

            for num in row:
                if num != '.':   #ignore '.'
                    if num in checked:
                        return False
                    checked.add(num)


        #check columns

        for col in range(9):   # we have 9 cols
            checked=set()
            for row in range(9):
                num=board[row][col]
                if num != '.':
                    if num in checked:
                        return False
                    checked.add(num)    

        #check 3x3 boxes

        for startRow in [0,3,6]:   #new boxes start at indices 0,3,6
            for startCol in [0,3,6]:
                checked = set()

                for r in range(startRow, startRow+3):    #to check 3x3
                    for c in range(startCol, startCol+3):
                        num=board[r][c]

                        if num != '.':
                            if num in checked:
                                return False
                            checked.add(num) 

                        
        return True

