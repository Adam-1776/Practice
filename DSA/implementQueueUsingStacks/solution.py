#https://leetcode.com/problems/implement-queue-using-stacks/

#Use two stacks, whenever we need to peek or dequeue, empty stack1 into stack2 so stack2 will have all the elements in reverse order
#Pop or peek from stack2 to get the bottom value of stack1. Then empty stack2 back into stack1. Pop() and peek() have O(n) time complexity
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.size = 0

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.empty() : return 0
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        dequeuedVal = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        self.size -= 1
        return dequeuedVal

    def peek(self) -> int:
        if self.empty() : return 0
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        peekedVal = self.stack2[-1]
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return peekedVal

    def empty(self) -> bool:
        return self.size == 0
    

#More efficient approach. Instead of repeatedly emptying stack1 and stack2 each time a push or pop is called, we only do it when necessary
#Obviously we have to empty stack1 into stack2 the first time pop or pull is called, but after that we hold on the values in stack2 for further peeks and pops.
#When stack2 is empty after repeated pops, we then empty stack1 into stack2 again. We always insert into stack1 since we cannot insert into stack2 without messing up its order.
#Since stack1 is supposed to have old elements to the left, and stack2 has old elements to the right.
#The amortized complexity is O(1), even though the first pop or peek takes O(n)
class MyQueue2:

    def __init__(self):
        self.inStack = [] #Stores elements that have not yet been reversed (old elements to the left)
        self.outStack = [] #Stores elements in reverse order (old elements to the right)
        self.size = 0

    def push(self, x: int) -> None:
        self.inStack.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.empty() : return -1 #Only proceed if the queue is not empty
        self.peek() #Populate outstack if it is currently empty
        self.size -= 1
        return self.outStack.pop() #Pop last element from outstack

    #This method empties instack into outstack ONLY if outstack is empty
    def peek(self) -> int:
        if self.empty() : return -1 #Only proceed if the queue is not empty
        if not self.outStack: #If outStack is empty...
            while self.inStack: #Completely empty inStack into outStack, which also reverses the order
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]
        

    def empty(self) -> bool:
        return self.size == 0




def main():
    myQueue = MyQueue2()
    myQueue.push(1); # queue is: [1]
    myQueue.push(2); # queue is: [1, 2] (leftmost is front of the queue)
    print(myQueue.peek()); # return 1
    print(myQueue.pop()); # return 1, queue is [2]
    print(myQueue.empty()); # return false
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method