from collections import defaultdict
#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 #longest substring with unique characters found so far
        setChars = set() #Set of all characters inside current window
        left = 0 #Left index of sliding window (inclusive)
        right = 0 #Right index of sliding window (inclusive)
        while (right < len(s)):
            if s[right] not in setChars: #We found a new character not in our window, increase window by one to the right
                setChars.add(s[right]) #Add this new character to our current set
                if len(setChars) > longest : longest = len(setChars) #If this is the longest substring we've seen so far, record that
                right += 1 #Increment the right index
            else: #We found a character already inside our window, we no longer have a substring with all unique characters
                while s[left] != s[right]: #To make our substring unique again, we have to shrink the window from the left, to delete everything
                    #up to and including where this character was already in our window
                    setChars.discard(s[left]) #Discard characters as we shrink our window from the left
                    left += 1 #Shrink our window from the left
                #The above while loop stops once we have reach the left character that's duplicate. We need to move past it to make our window unique again.
                #Important: notice how the repeating character is not discarded from the set!
                left += 1
                right += 1 #After incrementing left and right, our sliding window is unique again

        return longest

    #Same approach, slightly neater implementation of window shrinking
    def lengthOfLongestSubstring2(self, s: str) -> int:
        longest = 0 #longest substring with unique characters found so far
        setChars = set() #Set of all characters inside current window
        left = 0 #Left index of sliding window (inclusive)
        right = 0 #Right index of sliding window (inclusive)
        while (right < len(s)):
            if s[right] not in setChars: #We found a new character not in our window, increase window by one to the right
                setChars.add(s[right]) #Add this new character to our current set
                if len(setChars) > longest : longest = len(setChars) #If this is the longest substring we've seen so far, record that
                right += 1 #Increment the right index
            else: #We found a character already inside our window, we no longer have a substring with all unique characters
                while s[right] in setChars:
                    setChars.discard(s[left])
                    left += 1
                #left is now one index past where the repeating character.
                setChars.add(s[right]) #Since the repeating character was discarded, we have to add it. (We know right points to the same repeating character)
                right +=1

        return longest

def main():
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb")) #3

if __name__ == "__main__": #Entry point
    main() #Calling main method