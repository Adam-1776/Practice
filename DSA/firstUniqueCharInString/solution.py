from collections import Counter, defaultdict

#https://leetcode.com/problems/first-unique-character-in-a-string/


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = defaultdict(int)
        for char in s:
            dict1[char] += 1
        for i in range(0,len(s)):
            if dict1[s[i]] == 1:
                return i
        return -1

    #Slightly more concise solution using Counter
    def firstUniqChar2(self, s: str) -> int:
        count=Counter(s) #Counter constructor can count all objects in a list
        for i,j in count.items(): #Dictionary unpacking. i is the letter, and j is its count
            if j==1:
                return s.index(i) #Get the first index that has letter i
        return -1



def main():
    solution = Solution()
    print(solution.firstUniqChar("loveleetcode")) #2

if __name__ == "__main__": #Entry point
    main() #Calling main method