from collections import deque

#https://leetcode.com/problems/valid-parentheses/

class Solution:
    #A somewhat verbose implementation
    def isValid(self, s: str) -> bool:
        if len(s) < 2 : return False #String must have at least two characters to be balanced
        brackets = [] #Using this list like a stack
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[' :
                brackets.append(s[i])
            elif s[i] == ')' :
                if len(brackets) > 0 and brackets[len(brackets)-1] == '(':
                    brackets.pop()
                else:
                    return False
            elif s[i] == '}' :
                if len(brackets) > 0 and brackets[len(brackets)-1] == '{':
                    brackets.pop()
                else:
                    return False
            elif s[i] == ']' :
                if len(brackets) > 0 and brackets[len(brackets)-1] == '[':
                    brackets.pop()
                else:
                    return False
        return len(brackets) == 0

    #More concise solution using a dictionary and a deque
    def isValid2(self, s: str) -> bool:
        if len(s) < 2 : return False #Must have two characters to be balanced
        stack = deque() #Initialize an empty deque, we'll use it as a stack
        bracketMap = {'}':'{',')':'(',']':'['} #Set closing brackets as the key, since we lookup this dictionary when encountering closing brackets
        for i in range(len(s)):
            if s[i] in bracketMap.values(): #If we encounter an opening bracket ...
                stack.append(s[i]) #Add it to our stack
            elif s[i] in bracketMap.keys(): #Else if we encounter a closing bracket ...
                if stack and bracketMap[s[i]] == stack[-1]: #Check to make sure the stack isn't empty, and then
                    stack.pop() #see if the top of the stack has the matching opening bracket. If it does, we pop that opening bracket since we found its match
                else: #If the top of the stack does not have the matching opening bracket to the closing bracket we just found ...
                    return False #We have a mismatch, return false.
        return not stack #If the stack is empty, then everything matched. If there were mismatches, the stack has elements.
    
    #More concise solution using a dictionary and a deque
    def isValid3(self, s: str) -> bool:
        if len(s) < 2 : return False #Must have two characters to be balanced
        stack = deque() #Initialize an empty deque, we'll use it as a stack. Alternately you can use a list as a stack
        bracketMap = {'}':'{',')':'(',']':'['} #Set closing brackets as the key, since we lookup this dictionary when encountering closing brackets
        for char in s:
            if char in bracketMap.values():
                stack.append(char)
            elif char in bracketMap.keys():
                if stack and bracketMap[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack

    #Even more concise solution
    def isValid4(self, s: str) -> bool:
        if len(s) < 2 : return False
        stack = deque()
        bracketMap = {'}':'{',')':'(',']':'['}
        for char in s:
            if char in bracketMap.values(): #char is an opening bracket
                stack.append(char)
            else: #char is a closing bracket
                if not stack or bracketMap[char] != stack.pop():
                    return False
        return not stack #We expect the stack to be empty if parentheses are valid





def main():
    solution = Solution()
    print(solution.isValid("()[]{}")) #True
    print(solution.isValid2("()[]{}")) #True

if __name__ == "__main__": #Entry point
    main() #Calling main method