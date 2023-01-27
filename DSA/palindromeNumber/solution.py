#https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        intStr = str(x) #Converting int to str has linear time complexity with respect to the number of digits (for small integers)
        left = 0
        right = len(intStr) - 1
        while right > left : #Checking if the string is a palindrome once again has linear time complexity
            if intStr[left] != intStr[right] : return False
            left += 1
            right -= 1
        return True

    #Implementation without converting to string, a bit more efficient
    def isPalindrome2(self, x: int) -> bool:
        y = x #Saving original value of x
        if x < 0: return False #Negative numbers cannot be palindromes since the negative sign is only on one side
        sum = 0
        while x > 0:
            sum = (x % 10) + (sum * 10) #Take the rightmost digit of x, add it to our sum.
            x = x // 10 #Remove the rightmost digit of x
        #Above, we've set integer sum to be what x would be if read from right to left
        #To do this, we act like we're reading the digits from right to left,
        #even though we're reading from left to right in reality. Each time we add a new digit to the right
        #the value of the existing digits (stored in sum) go up by a factor of 10. For example, if we add the a digit
        #to the right of 12 so that it becomes 124 for example, the value of the two digits that were already there jump from 12 to 120
        #Similarly, if you remove the rightmost digit from a number, the value of the remaining digits is divided by 10.
        return sum == y


def main():
    solution = Solution()
    print(solution.isPalindrome(4554)) #True
    print(solution.isPalindrome2(845548)) #True

if __name__ == "__main__": #Entry point
    main() #Calling main method