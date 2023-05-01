#https://leetcode.com/problems/ugly-number-ii/

import math

class Solution:
    #Dynamic programming approach
    def nthUglyNumber(self, n: int) -> int:
        nums = [0] * n #This list stores all the ugly numbers we've deduced in order
        nums[0] = 1
        index2, index3, index5 = 0,0,0 #These variables represent the number of times prime factors 2,3, and 5 have been 'used' to arrive at the latest ugly number
        #Another point: the above variables represent the smallest index in nums that has NOT yet been multiplied by 2,3, or 5 to derive a new ugly number.
        #For example, if index2 = 2, this means that nums[2] has not yet been multiplied by 2 to derive a new ugly number. Since the only way to get new
        #ugly numbers is to multiply existing ugly numbers by 2, 3, or 5, we keep track of which ugly number has not yet been multiplied by 2,3, or 5 to get new
        #ugly numbers.
        #The above variables are initialized at zero since the first ugly number (1) doesn't have any prime factors 2,3, or 5
        for i in range(1,n):
            #In the line below, we find the next ugly number. Since we only ever multiply by 2,3, or 5, we know that we'll only get numbers that have those prime factors.
            nums[i] = min(nums[index2] * 2, nums[index3] * 3, nums[index5] * 5)
            if nums[i] == nums[index2] * 2:
                index2 += 1 #nums[index2] was multiplied by 2 to get a new ugly number. Increment index2
            if nums[i] == nums[index3] * 3:
                index3 += 1
            if nums[i] == nums[index5] * 5:
                index5 += 1
        return nums[n-1]
    
    #Below method does NOT work!! Including for demonstration purposes only.
    #Here, we try an approach where we pick the smallest multiple of 2,3, or 5 to go next in our list, instead of multiplying existing ugly numbers
    #The reason this doesn't work is because it does not exclude other prime factors. For example, this method includes 14. 14 is not an ugly number
    #because it has another prime factor seven. Again, the method below does NOT work.
    def nthUglyNumber2(self, n: int) -> int:
        nums = [0] * n
        nums[0] = 1
        index2, index3, index5 = 1,1,1
        i = 1
        while i < n:
            nums[i] = min(index2 * 2, index3 * 3, index5 * 5)
            print(f'nums[{i}] = {nums[i]}')
            if nums[i] == index2 * 2:
                index2 += 1
            if nums[i] == index3 * 3:
                index3 += 1
            if nums[i] == index5 * 5:
                index5 += 1
            i += 1
        return nums[n-1]
    
#The key to understanding this problem is that the only way to get a new ugly number is to *multiply an ugly number by 2,3 or 5.
#This is why we start off with an ugly number (1), and multiply by it 2,3, and 5 to get more ugly numbers. Also, each ugly number
#must be multiplied by 2,3, and 5 at some point as we progress along our discovery of new ugly numbers.

def main():
    solution = Solution()
    print(solution.nthUglyNumber(5, 2, 11, 13)) #10 is the fifth ugly number

if __name__ == "__main__": #Entry point
    main() #Calling main method