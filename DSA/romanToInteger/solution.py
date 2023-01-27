#https://leetcode.com/problems/roman-to-integer/

class Solution:

    #Linear time complexity with respect to number of roman digits
    def romanToInt(self, s: str) -> int:
        sum = 0
        i = 0
        while i < len(s):
            if s[i] == 'I': #Need to look ahead
                if i+1 < len(s): #Make sure there is a digit ahead of us
                    if s[i+1] == 'V': sum += 4; i+=1 #Need to increment the index to skip next digit, which we have accounted for
                    elif s[i+1] == 'X': sum += 9; i+=1 #Need to increment the index to skip next digit, which we have accounted for
                    else: sum += 1
                else: sum += 1
            elif s[i] == 'X':
                if i+1 < len(s):
                    if s[i+1] == 'L': sum += 40; i+=1 #Need to increment the index to skip next digit, which we have accounted for
                    elif s[i+1] == 'C': sum += 90; i+=1 #Need to increment the index to skip next digit, which we have accounted for
                    else: sum += 10
                else: sum += 10
            elif s[i] == 'C':
                if i+1 < len(s):
                    if s[i+1] == 'D': sum += 400; i+=1 #Need to increment the index to skip next digit, which we have accounted for
                    elif s[i+1] == 'M': sum += 900; i+=1 #Need to increment the index to skip next digit, which we have accounted for
                    else: sum += 100
                else: sum += 100
            elif s[i] == 'V' : sum += 5 #Don't need to look ahead for V, L, D, or M
            elif s[i] == 'L' : sum += 50
            elif s[i] == 'D' : sum += 500
            else : sum += 1000 #If it doesn't match I, X, C, V, L, or D, then it must be M
            i += 1 #Increment the index to move on
        return sum

    #More efficient and concise solution, still has linear complexity though
    #This approach takes advantage of the fact that a lesser digit will only ever precede a greater digit if it's for subtraction
    def romanToInt2(self, s: str) -> int:
        digitMap = {'I':1, 'V': 5, 'X': 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i = 0
        sum = 0
        while i < len(s):
            #print(s[i])
            sum += digitMap[s[i]] #Get the value of the current roman digit from the map
            #print(f'Adding {digitMap[s[i]]}')
            if i > 0 and digitMap[s[i-1]] < digitMap[s[i]] : #If the previous digit is lesser than the current digit ...
                sum -= digitMap[s[i-1]] * 2 #Important: If we realize we need to subtract the previous digit, we must subtract it twice!
                #We subtract twice because in the previous iteration we had added that previous digit erroneously. Example: In 'IV', the digit 'I' is not added, it is only subtracted
                #print(f'Subtracting {digitMap[s[i-1]]}')
            i += 1
        return sum

    


def main():
    solution = Solution()
    print(solution.romanToInt("MCMXCIV")) #1994
    print(solution.romanToInt2("MCMXCIV")) #1994

if __name__ == "__main__": #Entry point
    main() #Calling main method