#https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0 : return ""
        count = 0 #current index we're looking at
        prefix = "" #prefix we've found so far
        curLetter = '' #current letter we're looking at
        while True:
            if len(strs[0]) <= count : return prefix #Start with the first string, make sure it's long enough
            curLetter = strs[0][count] #Record the first string's character at the current index
            for word in strs: #Iterate over the rest of the words
                if len(word) <= count : return prefix #If any word is not long enough, the prefix cannot grow further
                elif word[count] != curLetter : return prefix #If any word's letter does not match the others, the prefix cannot grow further
            prefix += curLetter #If we reach this line, all the words have a common prefix uptil the index count. Append the current letter
            count += 1

    #A more concise implementation
    def longestCommonPrefix2(self, strs: list[str]) -> str:
        if len(strs) == 0 : return "" #If there are no strings in the list
        for i in range(len(strs[0])) : #Since the prefix cannot exceed the length of any string, iterate over the length of an arbitrary string
            curLetter = strs[0][i] #Get the current letter
            for word in strs: #Check all the strings to see if it matches this letter at the current index
                try: #By using try and except, we can automatically terminate if any of the strings are too short
                    if word[i] != curLetter : return strs[0][:i] #If a letter does not match, we return the prefix
                except IndexError:
                    return strs[0][:i] #Return the first i letters of any string if we counter an indexError (indicating a string is too short)
        return strs[0] #This line is only reached if len(strs[0]) == 0


def main():
    solution = Solution()
    print(solution.longestCommonPrefix(["flower","flow","flight"])) #fl
    print(solution.longestCommonPrefix2(["flower","flow","flight"])) #fl

if __name__ == "__main__": #Entry point
    main() #Calling main method