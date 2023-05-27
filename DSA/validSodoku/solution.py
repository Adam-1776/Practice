#https://leetcode.com/problems/valid-sudoku/

class Solution:
    #Traverse the entire board once, and check each cell to see if there's another cell with the same value
    #in the same row, column, and square. Immediately return False if such a cell is found
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        #Helper method that takes the row and column of a cell, and returns which square it's on (0 through 8)
        def getSquare(row: int, col: int) -> int:
            if (row // 3) < 1: #If it's in the first three rows
                return (col // 3)
            elif (row // 3) >= 1 and (row //3) < 2: #If it's in the middle three rows
                return 3 + (col // 3)
            else: #If it's in the last three rows
                return 6 + (col // 3)
        
        #More efficient helper method to return square number for a given cell. We're numbering the squares so that
        #its number is the number of squares above and to its left
        def getSquare2(row: int, col: int) -> int:
            return (3 * (row // 3)) + (col // 3)

        rowSetList = [set() for _ in range(9)] #Use list comprehension to create list of nine sets
        colSetList = [set() for _ in range(9)]
        squareSetList = [set() for _ in range(9)]

        for row in range(len(board)):
            for col in range(len(board[0])):
                value = board[row][col]
                if not value.isdigit() : continue #We ignore non-numeric cells
                square = getSquare(row,col) #Square range from 0 to 8
                if (value in rowSetList[row]) or (value in colSetList[col]) or (value in squareSetList[square]):
                    #print(f'Value {value} at board[{row}][{col}] is duplicate')
                    return False
                else:
                    rowSetList[row].add(value)
                    colSetList[col].add(value)
                    squareSetList[square].add(value)
        #If we make it here, then our board is a valid sodoku board
        return True

def main():
    board = [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    solution = Solution()
    print(solution.isValidSudoku(board)) #False since top left square has two cells with value 8

if __name__ == "__main__": #Entry point
    main() #Calling main method