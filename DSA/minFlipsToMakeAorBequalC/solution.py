#https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

class Solution:
    #Verbose method that converts the integers into binary strings, and compares each char in the string
    def minFlips(self, a: int, b: int, c: int) -> int:

        binA = a & 1
        print(type(binA))
        print(binA)

        binC = bin(c).replace("0b", "")
        binA = bin(a).replace("0b", "")
        binB = bin(b).replace("0b", "") #Convert A, B, C into binary strings
        length = max(len(binC), len(binA), len(binB)) #Get the maximum length of A, B, and C binary strings
        binC = binC.zfill(length)
        binA = binA.zfill(length)
        binB = binB.zfill(length) #Add as many leading zeroes as necessary to make all three binary strings the same length
        numFlips = 0
        for i in range(length):
            if binC[i] == "0": #If C is zero at this index
                if binA[i] != binC[i] and binB[i] != binC[i]: #Both A and B have one at this index
                    numFlips += 2
                elif binA[i] != binC[i] or binB[i] != binC[i]: #If either A or B have one at this index
                    numFlips += 1
            else: #If C is one at this index
                if binA[i] != binC[i] and binB[i] != binC[i]: #Both A and B have zero at this index
                    numFlips += 1

        return numFlips


    
    def minFlips2(self, a: int, b: int, c: int) -> int:
        numFlips = 0
        while a > 0 or b > 0 or c > 0:
            a_bit = a & 1 #Set a_bit to an integer equal to 0 or 1, matching the rightmost bit in a
            b_bit = b & 1
            c_bit = c & 1

            if c_bit ==  0: #If the current bit in c is zero...
                numFlips += a_bit + b_bit #We have to flip each of the ones in a and b to make them zero
            elif a_bit == 0 and b_bit == 0: #If current bit in c is one and both a and b are zero...
                numFlips += 1 #We can flip either the bit in a or b

            a = a >> 1
            b = b >> 1
            c = c >> 1
        
        return numFlips



def main():
    solution = Solution()
    print(solution.minFlips(2, 6, 5)) #3
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method