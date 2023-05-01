#https://leetcode.com/problems/ugly-number-iii/
#https://leetcode.com/problems/ugly-number-iii/solutions/387539/cpp-binary-search-with-picture-binary-search-template/
import math

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        #Condition: Are there at least n ugly numbers smaller than or equal to value?
        def countUglyNumbers(value):
            #Note: to help understand the additions and subtractions, look at the image in the solution link above
            #Basically, the duplicates are added thrice on line 12, and are deleted thrice on line 13.
            #However, we want to keep the intersections of a,b,c so we add it at the end of line 12
            count = (value//a) + (value//b) + (value//c) + (value//abc)
            count -= ((value//ab) + (value//bc) + (value//ac))
            #As a general principle, if there are three overlapping circles a,b,c the combined area excluding overlaps are:
            #F(N) = (a + b + c) - (a ∩ c + a ∩ b + b ∩ c) + (a ∩ b ∩ c)
            #We use this principle to find the number of ugly numbers greater than or lesser than value in this method
            return count >= n

        #Compute LCM for combinations of a,b,c using formula LCM(a,b) = (a*b)/GCD(a,b)
        ab = (a*b) // math.gcd(a,b) #LCM of a and b
        bc = (b*c) // math.gcd(b,c) #LCM of b and c
        ac = (a*c) // math.gcd(a,c) #LCM of a and c
        abc = (ab*c) // math.gcd(ab,c) #LCM of a, b, and c
        
        #Setup binary search to find the minimum value that satisfies nthUglyNumber(). This will be the kth ugly number.
        left, right = 1, (2 * 10**9) #Use the range given in the problem statement
        while left < right:
            mid = left + (right - left) // 2
            if countUglyNumbers(mid):
                right = mid
            else:
                left = mid + 1
        return left
    
    #Alternate solution that uses math.lcm() method
    def nthUglyNumber2(self, n: int, a: int, b: int, c: int) -> int:
        #Condition: Are there at least n ugly numbers smaller than or equal to value?
        def countUglyNumbers(value):
            count = (value//a) + (value//b) + (value//c) + (value//abc)
            count -= ((value//ab) + (value//bc) + (value//ac))
            return count >= n

        ab = math.lcm(a,b) #LCM of a and b
        bc = math.lcm(b,c) #LCM of b and c
        ac = math.lcm(a,c) #LCM of a and c
        abc = math.lcm(ab,c) #LCM of a, b, and c
        
        left, right = 1, (2 * 10**9)
        while left < right:
            mid = left + (right - left) // 2
            if countUglyNumbers(mid):
                right = mid
            else:
                left = mid + 1
        return left

def main():
    solution = Solution()
    print(solution.nthUglyNumber(5, 2, 11, 13)) #10 is the fifth ugly number

if __name__ == "__main__": #Entry point
    main() #Calling main method