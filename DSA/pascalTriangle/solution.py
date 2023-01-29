#https://leetcode.com/problems/pascals-triangle/

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

    #Same approach, but use a try catch to catch index errors.
    def generate2(self, numRows: int) -> list[list[int]]:
        if numRows < 1 : return None
        triangle = [[1]]
        for row in range(1,numRows) :
            numList = []
            for n in range(row+1) :
                try :
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
         


def main():
    solution = Solution()
    print(solution.generate2(5)) #[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


if __name__ == "__main__": #Entry point
    main() #Calling main method