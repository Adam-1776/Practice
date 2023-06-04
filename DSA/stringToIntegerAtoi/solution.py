#https://leetcode.com/problems/string-to-integer-atoi/


#Need to be cautious to handle strange and unexpected edgecases
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        result = 0
        sign = 1
        if s and s[0] == '-':
            sign = -1
            s = s[1:]
        elif s and s[0] == '+': #Use elif here so s[0] is only checked once
            s = s[1:]
        for digit in s:
            if digit.isdigit():
                result = (result * 10) + (ord(digit) - ord('0'))
            else:
                break
        result *= sign
        result = max(result, -2**31)
        result = min(result, (2**31)-1) #Limit result to 32 bits
        return result
            

def main():
    solution = Solution()
    print(solution.myAtoi("4193 with words")) #4193

if __name__ == "__main__": #Entry point
    main() #Calling main method