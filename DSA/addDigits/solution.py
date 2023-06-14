#https://leetcode.com/problems/add-digits/


class Solution:
    #This approach is linear with respect to number digits. This is a naive and somewhat unimpressive solution
    def addDigits(self, num: int) -> int:
        while num > 9:
            digitSum = 0
            while num != 0:
                digitSum += num % 10
                num //= 10
            num = digitSum
        return num
    

    #Very clever approach! This approach is called 'digit root' (need to research this further)
    # https://leetcode.com/problems/add-digits/solutions/1754040/c-recursion-and-iteration-and-o-1-approaches-fast-solutions/
    def addDigits2(self, num: int) -> int:
        if num == 0:
          return 0
        elif num % 9 == 0:
          return 9
        else:
          return num % 9



def main():
    solution = Solution()
    print(solution.addDigits(38)) #2
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method