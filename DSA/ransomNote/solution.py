#https://leetcode.com/problems/ransom-note/

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countMagazine = Counter(magazine)
        countRansom = Counter(ransomNote)
        for i,j in countRansom.items(): #Dictionary unpacking. i is the letter, and j is its count
            if countMagazine[i] < j:
                return False
        return True
            

def main():
    solution = Solution()
    print(solution.canConstruct("aa", "aab")) #True

if __name__ == "__main__": #Entry point
    main() #Calling main method