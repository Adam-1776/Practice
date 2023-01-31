#https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        #our intput, n, is just a normal integer
        bits = bin(n)[2:].zfill(32) #Convert this integer to a string representing its binary equivalent, add leading zeroes to make it 32 characters long
        bitsReversed = bits[::-1] #Reverse the string we created above
        x = int(bitsReversed, 2) #Convert our reversed binary string to an integer.
        return x

def main():
    solution = Solution()
    print(solution.reverseBits(54)) # 1811939328

if __name__ == "__main__": #Entry point
    main() #Calling main method