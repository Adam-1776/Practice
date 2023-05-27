#https://leetcode.com/problems/first-letter-to-appear-twice/

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        charSet = set()
        for letter in s:
            if letter in charSet:
                return letter
            else:
                charSet.add(letter)
        return None #This line should not be reached, since the problem statement
        #guarantees one letter that occurs twice
            

def main():
    solution = Solution()
    print(solution.repeatedCharacter("abccbaacz")) #c

if __name__ == "__main__": #Entry point
    main() #Calling main method