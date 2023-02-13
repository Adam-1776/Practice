#https://leetcode.com/problems/length-of-last-word/

class Solution:
    #Approach where we do not create a new string or list
    def lengthOfLastWord(self, s: str) -> int:
        wordLen = 0
        i = len(s) - 1
        letterFound = False
        while i >= 0: #Iterate from the last character of the string backwards
            if s[i] != ' ' : letterFound = True #If we have encountered a letter, it means we've moved past trailing whitespace
            if letterFound and s[i] == ' ' : return wordLen #If we've moved past trailing whitespace and now see a whitespace, we've covered the last word
            
            if letterFound : wordLen += 1 #Only increment wordLen if we've moved past the trailing whitespace
            i -= 1
        return wordLen

    #Approach using python built-in functions
    def lengthOfLastWord2(self, s: str) -> int:
        wordList = s.split() #Split the string into a list of words seperated by whitespace
        return len(wordList[-1]) #Return the length of the last word


def main():
    solution = Solution()
    print(solution.lengthOfLastWord("   fly me   to   the moon  ")) #4
    print(solution.lengthOfLastWord2("   fly me   to   the moon  ")) #4

if __name__ == "__main__": #Entry point
    main() #Calling main method