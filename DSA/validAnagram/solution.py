#https://leetcode.com/problems/valid-anagram/

from collections import Counter, defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False
        scount = Counter(s)
        tcount = Counter(t)
        return scount == tcount
    
    #Alternate solution using defaultdict
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False
        scount = defaultdict(int)
        tcount = defaultdict(int)
        for i in range(len(s)):
            scount[s[i]] += 1
            tcount[t[i]] += 1
        return scount == tcount
    
    
            

def main():
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram")) #True
    print(solution.isAnagram2("anagram", "nagaram")) #True

if __name__ == "__main__": #Entry point
    main() #Calling main method