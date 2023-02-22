#https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 : return s
        strList = [""] * numRows #Create a list of strings, one string for each row
        currRow = 0 #What row of the zig zag we are currently on
        direction = 1 #This integer is used to keep track of whether we're moving up in the zig zag or downwards
        for c in s:
            strList[currRow] += c
            currRow += direction #Move on to the next row (whichever direction that is)
            if currRow == numRows: #Need to change directions if we've exceeded the bounds of the zigzag downwards
                currRow = numRows - 2 #Our next insertion should be in the second last row, since we just inserted in the last row
                direction = -1 #We will now begin moving upwards
            elif currRow < 0: #Need to change directions if we've exceeded the bounds of the zigzag upwards
                currRow = 1 #Next insertion will be second row, since we just inserted in the first row
                direction = 1 #We will now begin moving downwards
        #After this loop, we have the characters belonging to each row of the zigzag stored in our list. We can concatenate them to find our answer
        return ''.join(strList)

def main():
    solution = Solution()
    print(solution.convert("PAYPALISHIRING", 3)) #PAHNAPLSIIGYIR

if __name__ == "__main__": #Entry point
    main() #Calling main method