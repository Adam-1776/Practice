import math

#https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        #our intput, n, is just a normal integer
        bits = bin(n)[2:].zfill(32) #Convert this integer to a string representing its binary equivalent, add leading zeroes to make it 32 characters long
        bitsReversed = bits[::-1] #Reverse the string we created above
        x = int(bitsReversed, 2) #Convert our reversed binary string to an integer.
        return x

    #Implementation without hand-written logic instead of built-in functions
    def reverseBits2(self, n: int) -> int:
        i = 0
        bitList = [0] * 32 #List to store binary representation of n
        while n > 0 : #Convert out integer to binary
            bitList[31 - i] = n % 2 #Populate the list from right to left, since we're processing digits from right to left
            n = n // 2
            i += 1
        bitListReversed = bitList[::-1] #Reverse the binary list
        sum = 0
        place = 0 #Which place in the binary number we're at, starting from the right and with zero indexing
        for d in reversed(bitListReversed) : #Convert the reversed binary representation back to an integer
            sum += d * (2 ** place)
            place += 1
        return sum

def main():
    solution = Solution()
    #print(solution.reverseBits(54)) # 1811939328
    print(solution.reverseBits2(11))

if __name__ == "__main__": #Entry point
    main() #Calling main method