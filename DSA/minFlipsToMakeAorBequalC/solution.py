#https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
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



def main():
    solution = Solution()
    print(solution.minFlips(2, 6, 5)) #3
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method