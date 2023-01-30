import re

#https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        val = s.lower() #Make it case insensitive
        cleanstr = ""
        for i in val: #Only add alphanumeric characters
            if (ord(i) >= ord('a') and ord(i) <= ord('z')) or (ord(i) >= ord('0') and ord(i) <= ord('9')) :
                cleanstr += i
        l = 0
        r = len(cleanstr) - 1
        while l < r : #Check if it's a palindrome
            if cleanstr[l] != cleanstr[r] : return False
            l += 1
            r -= 1
        return True

    #More concise solution using regex
    def isPalindrome2(self, s: str) -> bool:
        data = re.sub(r'[^0-9a-zA-Z]', '', s.lower()) #Replacing these regex characters with nothing (i.e. deleting them)
        l = 0
        r = len(data) - 1
        while l < r : #Check if it's a palindrome
            if data[l] != data[r] : return False
            l += 1
            r -= 1
        return True


def main():
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama")) #True
    print(solution.isPalindrome2("A man, a plan, a canal: Panama")) #True

if __name__ == "__main__": #Entry point
    main() #Calling main method