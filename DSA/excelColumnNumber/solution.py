#https://leetcode.com/problems/excel-sheet-column-number/
#https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    #Basically we treat columnTitle like a base26 number and convert it to base10
    def titleToNumber(self, columnTitle: str) -> int:
        column = 0 #Base 10 representation of columnTitle
        digit = 0 #Which place in the string we're looking at, starting from the right and with zero indexing
        for c in reversed(columnTitle) :
            column += (ord(c) - ord('A') + 1) * (26 ** digit) #Formula to find the base10 'value' of a digit in a base26 number
            #NOTE: Above, we add one to the digit because this numbering system has no zero. The smallest 'digit' (i.e. A) represents 1
            digit += 1
        return column

    def convertToTitle(self, columnNumber: int) -> str:
        columnTitle = ""
        while columnNumber > 0 :
            columnNumber -= 1 #Decrement by one, since the first alphabet 'A' represents 1, not 0
            letter = columnNumber % 26
            columnTitle += chr(letter + ord('A'))
            columnNumber = columnNumber // 26
        return columnTitle[::-1] 

def main():
    solution = Solution()
    print(solution.titleToNumber("BCA")) # 1431
    print(solution.convertToTitle(1431)) # BCA

if __name__ == "__main__": #Entry point
    main() #Calling main method