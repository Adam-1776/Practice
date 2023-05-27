#https://leetcode.com/problems/pascals-triangle/
#https://leetcode.com/problems/pascals-triangle-ii/solutions/

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows < 1 : return None
        triangle = [[1]]
        for row in range(1,numRows) :
            numList = []
            for n in range(row+1) :
                #print(f'row = {row} and n = {n}')
                #print(str(triangle))
                val1 = triangle[row-1][n] if n < len(triangle[row-1]) else 0
                val2 = triangle[row-1][n-1] if n > 0 else 0
                numList.append(val1 + val2)
            triangle.append(numList[:]) #The list append method only copies the pointer by default. We have to use [:] to append a new copy
            #We need create a new copy of numList since we will overwrite numList in the next row
        return triangle

    #Does NOT work, same approach, but attempted a try catch to catch index errors.
    def generate2(self, numRows: int) -> list[list[int]]:
        if numRows < 1 : return None
        triangle = [[1]]
        for row in range(1,numRows) :
            numList = []
            for n in range(row+1) :
                val1 = 0
                val2 = 0
                try : #No index error is caught because negative indexes are valid in python, they just start counting from the back!
                    val1 = triangle[row-1][n]
                except IndexError: 
                    val1 = 0 
                try : 
                    val2 = triangle[row-1][n-1]
                except IndexError : 
                    val2 = 0
                numList.append(val1 + val2)
            triangle.append(numList[:]) #The list append method only copies the pointer by default. We have to use [:] to append a new copy
            #We need create a new copy of numList since we will overwrite numList in the next row
        return triangle

    #Space efficient solution for Pascal II, only stores one row at a time instead of the whole triangle
    def getRow(self, rowIndex: int) -> list[int]:
        currRow = 0
        currRowList = [1]
        while currRow < rowIndex:
            nextRow = []
            currRow += 1
            for i in range(0, currRow + 1):
                leftParent = 0 if i-1 < 0 else currRowList[i-1]
                rightParent = 0 if i > len(currRowList) - 1 else currRowList[i]
                nextRow.append(leftParent + rightParent)
            currRowList = nextRow
        return currRowList
         


def main():
    solution = Solution()
    print(solution.generate2(5)) #[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


if __name__ == "__main__": #Entry point
    main() #Calling main method