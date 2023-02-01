from math import log10
from math import log
from math import isclose

#https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0 : return False
        return (log10(n) / log10(3)).is_integer()

    #Alternate method using math.isclose()
    def isPowerOfThree2(self, n: int) -> bool:
        logVal = log(n,3) #Probably has strange floating point behavior
        return isclose(logVal,round(logVal)) #If logVal is very close to its rounded integer, then logVal should have been an integer


def main():
    solution = Solution()
    print(solution.isPowerOfThree(243))
    print(solution.isPowerOfThree2(243))

if __name__ == "__main__": #Entry point
    main() #Calling main method