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

    #Another two pointers approach
    def isPalindrome3(self, s: str) -> bool:
        seq = list(s.lower())
        l, r = 0, len(seq)-1
        while l < r:
            while l < r and (not seq[l].isalnum()): #We have to keep checking our main condition l < r since we are updating the pointers in this loop
                l += 1
            while l < r and (not seq[r].isalnum()):
                r -= 1
            #After the above two loops, l and r will point to the latest alphanumeric characers that not been compared from the left and right respectively, OR l and r will be equal
            if seq[l] != seq[r]:
                print(f'{l} and {r} are false')
                return False
            l += 1
            r -= 1
        return True


def main():
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama")) #True
    print(solution.isPalindrome2("A man, a plan, a canal: Panama")) #True

if __name__ == "__main__": #Entry point
    main() #Calling main method