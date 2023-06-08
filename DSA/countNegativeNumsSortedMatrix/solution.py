#https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/


class Solution:
    #Staircase approach starting from top right corner. In each iteration, we move left some columns, and down one row.
    #This is why the time complexity is O(numRows + numCols). The key to the problem is to add the number of each zeroes encountered
    #in each row one by one.
    def countNegatives(self, grid: list[list[int]]) -> int:
        numNegatives = 0
        numRows = len(grid)
        numCols = len(grid[0])
        currRow = 0
        currCol = numCols - 1 #Start from top right corner
        while currRow < numRows:
            while currCol >= 0 and grid[currRow][currCol] < 0: #Keep going till currCol no longer points to a negative value
                currCol -= 1
            #currCol now points to the rightmost non-negative value, or it equals -1 if all values in the row are negative
            numNegatives += numCols - currCol - 1 #Add the number of negative values we encountered in this row
            print(f'{currRow} and {currCol} and {numNegatives}')
            currRow += 1
        return numNegatives



def main():
    solution = Solution()
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

    print(solution.countNegatives(grid))
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method