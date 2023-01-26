#https://leetcode.com/problems/reverse-string-ii/

class Solution:
    #Simple implementation, not the most efficient
    def reverseStr(self, s: str, k: int) -> str:
        #In the line below, we use list comprehension to split the string into a list of strings with length 2*k
        #The last string in this list may be shorter than 2*k for obvious reasons. The technique above works because
        #there is no out of bounds index error in string clicing. If you do str[i,k] and k greater than len(str), it will
        #simply stop at the end of str.
        parts = [s[i:i+(2*k)] for i in range(0,len(s),2*k)]
        #below we use a lambda that concatenates the reverse of the first k characters in the string with the rest of the string.
        #The map() method applies this lambda to every string in the list. We then join them using "".join() to create the string. 
        return "".join(map(lambda i: i[k-1::-1]+i[k:] , parts))

    #More drawn-out approach
    def reverseStr2(self, s: str, k: int) -> str:
        def reverse(left: int, right: int, s: list): #Child function to reverse list from index left to right, both inclusive
            if right >= len(s) : right = len(s) - 1 #Keep going till the end of the list, in case the right index is out of bounds
            while (left < right):
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        
        listChars = list(s) #Convert the string to a list as-is
        for i in range(0, len(listChars), 2*k): #Iterate over indexes 0 to the end of the list, jumping 2*k in each iteration
            reverse(i,i+k-1,listChars) #Reverse all characters from i to i+k-1. We subtract one because our reverse method works inclusively for both indexes
        
        return "".join(listChars) #Return this list after converting it back to a string.

    #Recursive approach, more efficient
    def reverseStr3(self, s: str, k: int) -> str:
        if len(s)<(k):return s[::-1] #Base case 1: need to reverse the entire string
        if len(s)<(2*k):return (s[:k][::-1]+s[k:]) #Base case 2: We are in the last segment of the string, reverse first k characters of this segment
        #The line below is only reached if there are more characters to the right that need to be processed.
        return s[:k][::-1]+s[k:2*k]+self.reverseStr(s[2*k:],k)  #Concatenate our current processed segment with the results for the rest of the string. 

def main():
    solution = Solution()
    print(solution.reverseStr("abcdefg", 2)) #"bacdfeg"
    print(solution.reverseStr2("abcdefg", 2)) #"bacdfeg"

if __name__ == "__main__": #Entry point
    main() #Calling main method