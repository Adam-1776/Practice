#https://leetcode.com/problems/power-of-two/

class Solution:
    #O(log(n)) time complexity for obvious reasons
    def isPowerOfTwo(self, n: int) -> bool:
        num = 1
        while num < n:
            num *= 2
        return num == n 

    #O(1) time complexity
    #Notice that all powers of two have only a single one in their binary form, for example 16 = ...010000
    #One minus a power of two would therefore be all ones, for example 15 = ...01111
    #If you AND n and n-1, if n is a power of two the result will be zero as you can see
    def isPowerOfTwo2(self, n: int) -> bool:
        if n <= 0:
            return False
        return n & (n-1) == 0

def main():
    solution = Solution()
    print(solution.isPowerOfTwo(16))
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method