#https://leetcode.com/problems/isomorphic-strings/

class Solution:
    #The key to this problem is that there must be one-to-one mapping between the letters in both strings
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False #This line is actually optional since the problem guarantees both strings are of equal length
        charMaps = dict()
        charMapt = dict() #Need two dictionaries to verify one-to-one mapping
        for i in range(len(s)):
            if s[i] not in charMaps and t[i] not in charMapt: #Encountered new letters
                charMaps[s[i]] = t[i]
                charMapt[t[i]] = s[i] #Add both letters to their respective dictionaries for one-to-one mapping
            elif s[i] in charMaps and t[i] not in charMapt: #If only letter is in a dictionary...
                return False #One-to-one mapping has been violated, return False
            elif t[i] in charMapt and s[i] not in charMaps: #If only letter is in a dictionary...
                return False #One-to-one mapping has been violated, return False
            elif charMaps[s[i]] != t[i] or charMapt[t[i]] != s[i]: #Mismatch case
                return False

        return True #We only exit the loop and reach this line if they are isomorphic strings

    #Alternate, very clever solution. Possibly less efficient though since using the index() method repeatedly is inefficient 
    def isIsomorphic2(self, s: str, t: str) -> bool:
        map1 = []
        map2 = []
        for letter in s:
            map1.append(s.index(letter)) #Append the first index where letter occurs in string s
        for letter in t:
            map2.append(t.index(letter)) #Append the first index where letter occurs in string t
        print(map1)
        print(map2)
        return map1 == map2

def main():
    solution = Solution()
    print(solution.isIsomorphic("paper", "title")) #True

if __name__ == "__main__": #Entry point
    main() #Calling main method