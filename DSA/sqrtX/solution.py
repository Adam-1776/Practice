#https://leetcode.com/problems/sqrtx/

class Solution:
    #Linear time complexity, not the most efficient
    def mySqrt(self, x: int) -> int:
        n = 1
        while n*n <= x :
            n+=1
        return n - 1

    #Uses binary search, has O(logn) time complexity
    def mySqrt2(self, x: int) -> int:
        if x == 1 : return 1
        l = 1
        r = x
        mid = 1
        #We know that the square root must be between 1 and x, so we set those as our search area for now
        while True : #We can use an infinite loop here because we know every positive integer must have a square root we can find
            mid = (l + r) // 2 #Integer division
            #print(f'l = {l} and r = {r} and mid = {mid}')
            if mid * mid <= x and (mid+1) * (mid+1) > x : #We're looking for the rounded down integer value
                return mid
            elif x / mid > mid : #If our mid is too small ...
                l = mid
            else : #If our mid is too big ...
                r = mid

    #More concise approach, uses binary search template to find the greatest integer that meets the condition mid^2 <= x
    def mySqrt3(self, x: int) -> int:
        l, r = 1, x+1
        while l < r:
            mid = l + (r - l) // 2
            if mid * mid <= x:
                l = mid + 1
            else:
                r = mid
        return l-1

         


def main():
    solution = Solution()
    print(solution.mySqrt(101)) #10

if __name__ == "__main__": #Entry point
    main() #Calling main method