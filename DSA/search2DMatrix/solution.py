#https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    #Perform two binary searches, one to find the column and one to find the row
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        numRows, numCols = len(matrix), len(matrix[0])
        left, right = 0, numRows
        #Perform binary search to see which row the target value is above
        #This search finds the first row who's starting integer is greater than the target
        while left < right:
            mid = left + (right - left) // 2
            if matrix[mid][0] > target:
                right = mid
            else:
                left = mid + 1

        #Now, the target value should in row (left - 1)
        searchRow = left - 1
        #print(f'We believe the target value should be in row {searchRow}')
        #Perform binary search to find the smallest index whose value is greater than or equal to the target
        left, right = 0, len(matrix[searchRow])
        while left < right:
            mid = left + (right - left) // 2
            if matrix[searchRow][mid] >= target:
                right = mid
            else:
                left = mid + 1
        #print(f'Landed at matrix[{searchRow}][{left}]')
        if left >= len(matrix[searchRow]): return False #necessary to prevent out of bounds error when the target is greater than everything in the row
        return matrix[searchRow][left] == target



    #Same approach, slightly different binary search condition
    def searchMatrix2(self, matrix: list[list[int]], target: int) -> bool:
        numRows, numCols = len(matrix), len(matrix[0])
        left, right = 0, numRows
        #Perform binary search to see which row the target value is above
        #This search finds the first row who's starting integer is greater than the target
        while left < right:
            mid = left + (right - left) // 2
            if matrix[mid][0] > target:
                right = mid
            else:
                left = mid + 1

        #Now, the target value should in row (left - 1)
        searchRow = left - 1
        #print(f'We believe the target value should be in row {searchRow}')
        #Perform binary search to find the smallest index whose value is greater than the target
        left, right = 0, len(matrix[searchRow])
        while left < right:
            mid = left + (right - left) // 2
            if matrix[searchRow][mid] > target:
                right = mid
            else:
                left = mid + 1
        #Left should now be one index greater than the target, if it exists
        left -= 1 #Left should now point to the target if it exists
        #print(f'Landed at matrix[{searchRow}][{left}]')
        return matrix[searchRow][left] == target
    

    #Basically, we imagine that instead of a 2D matrix, we have a single long list. We perform a normal binary search on this
    #hypothetical list, and use a helper method to convert the index of this hypothetical list to the actual indexes it
    #would correspond to in our matrix
    def searchMatrix3(self, matrix: list[list[int]], target: int) -> bool:
        numRows, numCols = len(matrix), len(matrix[0])

        #Helper method to convert the index of the hypothetical list to the indexes of the 2D matrix
        def getIndexes(index: int) -> list[int]:
            row = index // (numCols)
            col = index % numCols
            #print(f'For index {index}, row and col are {row}, {col}')
            return [row, col]

        left, right = 0, (numRows * numCols) #left is 0, right is number of values in the matrix

        while left < right:
            mid = left + (right - left) // 2
            row, col = getIndexes(mid)[:2] #List unpacking to get actual indexes of mid
            if matrix[row][col] >= target:
                right = mid
            else:
                left = mid + 1

        row, col = getIndexes(left)[:2]
        if col >= numCols or row >= numRows: return False
        return matrix[row][col] == target

def main():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    solution = Solution()
    print(solution.searchMatrix(matrix, 13)) #False

if __name__ == "__main__": #Entry point
    main() #Calling main method