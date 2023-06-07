#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

#This problem is just simple string matching
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenHaystack = len(haystack)
        lenNeedle = len(needle)
        for i in range(lenHaystack - lenNeedle + 1): #Check all starting indexes that needle could possibly start from in haystack
            found = True
            for j in range(lenNeedle): #Start string matching starting from index i
                if haystack[i+j] != needle[j]: #Break if we determine that haystack cannot start from index i
                    found = False
                    break
            if found: return i
        return -1
    

    #Solution using built-in python method
    def strStr2(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)



def main():
    solution = Solution()
    print(solution.strStr("sadbutsad", "sad"))
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method