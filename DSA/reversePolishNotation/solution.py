#https://leetcode.com/problems/evaluate-reverse-polish-notation/

import math

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        stack = [] #This stack will contain all the numbers, as well as result of prior computed expressions, that are in line for further operation
        #When we encounter an operator, we replace the top two elements in the stack with the result of the operation. Note that the stack does not contain
        #operators, only numbers. These numbers could be directly from the tokens list, or numbers that we computed
        for token in tokens:
            if token not in ["-", "*", "+", "/"]: #If we encounter a number...
                stack.append(token) #Simply append it since it is in line for further operation
                #print(f'Encountered number {token} and current stack is {stack}')

            else: #If we encounter an operator...
                operator = token
                right = int(stack.pop())
                left = int(stack.pop()) #The last two elements in the stack will be operated upon
                #We convert our answer to a string, since that's the format we are using in this problem
                if operator == "+":
                    stack.append(str(left + right)) #We have replaced the last two elements in the stack with the result of the operation performed upon them
                elif operator == "-":
                    stack.append(str(left - right)) #We have replaced the last two elements in the stack with the result of the operation performed upon them
                elif operator == "*":
                    stack.append(str(left * right)) #We have replaced the last two elements in the stack with the result of the operation performed upon them
                else:
                    stack.append(str(math.trunc(left / right))) #Do float division and trucate to zero using math.trunc, since the problem demands it
                #print(f'Encountered operator {token} and current stack is {stack}')
        #We have run out of numbers and operators. The stack now only contains the result of the entire expression. In theory, it could be continued to be used if the expression
        #was longer.
        return int(stack.pop())


#The key this problem is the fact that whenever an operator is encountered, it operates on the two most recent numbers or expressions that came before it.
#Since we perform the operation and update the stack each time an operator is encountered, further operators will act upon the result of prior expressions instead of necessarily
#the prior two numbers in the original expression.
def main():
    solution = Solution()
    print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method