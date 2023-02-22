#https://leetcode.com/problems/reverse-integer/

import math


class Solution:
    #This solution works, but it's inefficient and uses integer variables that can exceed 32 bits
    def reverse(self, x: int) -> int:
        isNegative = x < 0
        reverseStr = ""
        if isNegative:
            reverseStr = "-" + str(x*-1)[::-1] #Make the integer positive and convert it into a string, reverse it, and add the negative sign
        else:
            reverseStr = str(x)[::-1] #If the integer is positive, simply convert it to a string and reverse it
        reverseInt = int(reverseStr) #Convert the string to an integer. This will automatically take care of any leading zeroes in the string
        if reverseInt > (2**31 - 1) or reverseInt < (-1 * 2**31) : #Check if our integer is outside the bounds of 32 bit integers
            return 0
        else:
            return reverseInt

    #This solution fits the spirit of the problem since it does not store integers exceeding 32 bits
    def reverse2(self, x: int) -> int:
        reverseInt = 0
        maxInt = 2**31 - 1 #Biggest 32 bit signed integer
        minInt = -1 * 2**31 #Smallest 32 bit signed integer
        #Reverse the digits, works even with negative integers
        while x != 0: #We only enter this while loop when there is another digit left to process
            nextDigit = int(math.fmod(x,10)) #Use fmod because modulus is weird in python with negative numbers
            #Below if condition is met if reverseInt will exceed maxInt when the next digit is added
            if (reverseInt > maxInt//10) or (reverseInt//10 == maxInt//10 and nextDigit > int(math.fmod(maxInt,10))):
                return 0 #Return zero if adding the next digit would cause an overflow
            #Below if condition is met if reverseInt will fall below minInt when the next digit is added
            if (reverseInt < int(minInt/10)) or (reverseInt//10 == int(minInt/10) and nextDigit < int(math.fmod(minInt,10))):
                return 0 #Return zero if adding the next digit would cause an overflow
            reverseInt = (reverseInt*10) + nextDigit
            #Since our result should have integers in reverse order, every time we append a new integer it goes in the one's place, and the other places get multiplied by 10
            x = int(x / 10)
        return reverseInt


def main():
    solution = Solution()
    print(solution.reverse(-123)) #-321
    print(solution.reverse(120)) #21
if __name__ == "__main__": #Entry point
    main() #Calling main method