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

    #Implementation without converting to string, more efficient
    def isPalindrome2(self, x: int) -> bool:
        y = x #Saving original value of x
        if x < 0: return False
        sum = 0
        while x > 0:
            sum = (x % 10) + (sum * 10) #Take the rightmost digit of x, add it to our sum.
            x = x // 10 #Remove the rightmost digit of x
        #Above, we've set integer sum to be what x would be if read from right to left
        #To do this, we act like we're reading the digits from right to left,
        #even though we're reading from left to right in reality. Each time we add a new digit
        #we the value of the existing digits (stored in sum) go up by a factor of 10.
        return sum == y


def main():
    solution = Solution()
    print(solution.isPalindrome(4554)) #True

if __name__ == "__main__": #Entry point
    main() #Calling main method