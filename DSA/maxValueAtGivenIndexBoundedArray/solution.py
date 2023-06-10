#https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array


class Solution:
    #Consecutive elements can have difference 0 or 1
    #each element must be positive ( > 0 )
    #sum of all elements <= maxSum
    #num[Index] should be the greatest
    #O(log(n)) complexity since we're doing binary search and condition() runs in constant time
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def condition(indexVal):
            indexVal -= 1 #Decrement indexVal because we have already accounted for all elements being one or greater
            arrSum = n #Sum of array is n to start with, since all elements are one one or greater
            #Basically, we will calculate on the basis of elements 'on top' of one. So for our purposes a value of 0 is acceptable
            b = max(indexVal-index, 0) #Smallest element on the lefthand side (there are index elements to the left of this index)
            arrSum += (indexVal + b) * (indexVal-b+1) // 2 #Incrememt sum of [b, b+1,...indexVal] to arrSum
            b = max(indexVal-(n-index-1), 0) #Smallest element on righthand side (there are (n-index-1) elements to the right of this index)
            arrSum += (indexVal+b)*(indexVal-b+1) // 2 #Increment sum of [b, b+1,...indexVal] to arrSum
            arrSum -= indexVal #Subtract by indexVal because it was added twice 
            ret = arrSum <= maxSum #If the sum of the array with value at index being indexVal is less than maxSum, indexVal is compliant
            #print(f'Returning {ret} for {indexVal} and sum {arrSum}')
            return ret


        #Find the maximum value of indexVal such that condition() is true using binary search
        l, r = 1, maxSum+2 #Minimum possible value is 1, setting that as l. Had to give maxSum+2 as r for some reason to pass all test cases
        while l < r:
            mid = l + (r - l) // 2
            if condition(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1



def main():
    solution = Solution()
    print(solution.maxValue(4, 2, 6)) #2
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method