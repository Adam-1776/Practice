#https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        if (r * c) != (len(mat) * len(mat[0])): #If requested dimensions are not possible...
            return mat #return original matrix
        newMatrix = [] #New 2D matrix
        newRow = [] #An individual row in the new matrix
        newRowCount = 0 #Number of items in the current row
        for row in mat:
            for cell in row: #Traverse original matrix row by row
                newRow.append(cell) #Append to the current row for our new matrix
                newRowCount += 1
                if newRowCount == c: #We've hit the requested row size, so time to move onto the next row
                    newMatrix.append(list(newRow)) #Add this completed row to the the matrix
                    newRowCount = 0 #Resetting the newRow list for the next row we'll add to new matrix
                    newRow = []
        return newMatrix
            

def main():
    solution = Solution()
    print(solution.matrixReshape([[1,2],[3,4]], r = 1, c = 4)) #[[1, 2, 3, 4]]

if __name__ == "__main__": #Entry point
    main() #Calling main method