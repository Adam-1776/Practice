#https://leetcode.com/problems/reverse-words-in-a-string/
#https://leetcode.com/problems/reverse-words-in-a-string-ii/
#https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

    def reverseWordsII(self, s: list[str]) -> list[str]:

        def reverse(leftt: int, right: int): #This is a child function inside reverseWordsII
            print(f'reverse was called with {leftt} and {right}')
            while leftt < right :
                s[leftt], s[right] = s[right], s[leftt] #This child function can modify list s even though
                leftt += 1 #it belongs to the parent function, since lists are mutable
                right -= 1 #This child method reverses a list from index leftt to right, both inclusive
    
        #Note: This technique only works because we know there are no leading or trailing spaces, and each word is seperated by one word only.
        #We use a two pointers approach. Use left as one pointer, and variable i as the other.
        left = 0 #left is the leftmost index that contains a letter, and has not been reversed yet. We know it starts with 0 since there is no leading whitespace.
        for i in range(0,len(s)):
            if s[i] == ' ': #We have reached the end of a word
                reverse(left, i-1) #Reverse the list from left, to the last index of the word we just found
                left = i+1 #We know that the the next word must start in the next index, since each word is seperated by one space.
        
        reverse(left ,len(s)-1) #The last word was not reversed in the above loop, must do it here
        reverse(0,len(s)-1) #Reversing the entire string. This unreverses each individual word and reverses the order in which they are present in the list.
        return s

    def reverseWordsIII(self, s: str) -> str:

        def reverse(s: str) -> str: #We define this child function to use later in the map function
            return s[::-1]

        wordArr = s.split() #wordArr is a list of all the words in string s
        #map takes each element of wordArr, and applies our reverse function on it. It works with any iterable including lists.
        return " ".join(map(reverse,wordArr)) #We then use the " ".join method to convert this list back to a string, where each element of the list is seperated by one space. 

    #Does the same thing as reverseWordsIII, but uses a list comprehension approach
    def reverseWordsIII2(self, s: str) -> str:
        list = [i[::-1] for i in s.split()]
        #Create a new list as follows: take each string in the list returned by s.split(), reverse it, and add it to our new list.
        #Works similarly to the map approach we used in the implementation above.
        return " ".join(list) #We have to convert this new list back to a string.

    #Does the same thing as reverseWordsIII, but uses a lambda function
    def reverseWordsIII3(self, s: str) -> str:
        #One line solution: put a lambda inside map() that reverses the string, and pass s.split() as the other parameter to map()
        #the map() function returns an iterable. We convert this to a string using " ".join()
        return " ".join(map(lambda i : i[::-1], s.split()))
    
    


def main():
    solution = Solution()
    print(solution.reverseWords("the sky is blue")) #"blue is sky the"
    print(solution.reverseWordsII(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))
    #["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
    print(solution.reverseWordsIII("the sky is blue")) #"eht yks si eulb"
    print(solution.reverseWordsIII2("the sky is blue")) #"eht yks si eulb"
    print(solution.reverseWordsIII3("the sky is blue")) #"eht yks si eulb"


if __name__ == "__main__": #Entry point
    main() #Calling main method