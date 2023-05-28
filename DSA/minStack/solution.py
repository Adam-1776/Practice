#https://leetcode.com/problems/min-stack/

#Use two stacks to find minimum value in O(1)
#The reason this method works is because we cannot remove the minimum value from any random index from the stack, we can only remove
#the smallest value if it's currently at the top of the stack. The top of the minStack is the smallest value in the stack at the time.
#When we pop the stack, it's equivalent to 'going back in time' to before that element was inserted, so we pop the minStack to see which
#was the smallest element at that time. 
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        #Append the current val if it's the smallest value we've seen so far, else append the top of the stack
        self.minStack.append(min(val, self.minStack[-1] if self.minStack else val))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return -1

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]



def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method