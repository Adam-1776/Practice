#https://leetcode.com/problems/ugly-number/

class Solution:
    def isUgly(self, n: int) -> bool:
        #If n does not have any prime factors besides 2, 3, and 5, return True
        if n <= 0 : return False
        while n%2 == 0:
            n /= 2
        while n%3 == 0:
            n /= 3
        while n%5 == 0:
            n /= 5
        #In the loops above, we've divided n by 2, 3, and 5 as many times as we can. If there are other prime factors
        #then n will not be 1.
        return n == 1

def main():
    solution = Solution()
    print(solution.nthUglyNumber(5, 2, 11, 13)) #10 is the fifth ugly number

if __name__ == "__main__": #Entry point
    main() #Calling main method