#https://leetcode.com/problems/implement-stack-using-queues/

from collections import deque

#Implement a stack using two queues
#O(1) complexity for push, O(n) complexity for pop or top
class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        self.length = 0 #Number of elements in the stack
        self.currQueue = 1 #Which queue is currently holding our elements. Start with queue 1

    def push(self, x: int) -> None:
        if self.currQueue == 1: #Append to whichever queue we're currently using to hold the elements
            self.queue1.append(x)
        else:
            self.queue2.append(x)
        self.length += 1 #Increment the length since we just appended

    def pop(self) -> int:
        self.length -= 1 #Decrement the length by one since we're performing a deletion
        if self.currQueue == 1: #If we're currently holding in queue1...
            for _ in range(self.length): #Take all but the last elements from queue1 and append it to queue2
                self.queue2.append(self.queue1.popleft()) #Notice that the last element will be left in queue1, since we decremented self.length above
            self.currQueue = 2 #queue2 not holds our remaining elements, so set this variable accordingly
            return self.queue1.pop() #queue1 now only holds the last element that was originally present in queue1 since we called popleft() length-1 times...
            #We return queue1.pop() to return the top of the stack and also empty out queue1. Now queue2 holds all our remaining elements
        
        else: #Exact same logic as above, only this time queue2 holds our elements at first. We will end up with queue1 holding the remaining values after deletion
            for _ in range(self.length):
                self.queue1.append(self.queue2.popleft())
            self.currQueue = 1
            return self.queue2.pop()
        

    #Pretty much the same logic as pop() except we don't delete the last value in the queue. Instead we save it, and then insert it to the back of the new current queue
    def top(self) -> int:
        if self.currQueue == 1:
            for _ in range(self.length - 1): #We move elements from queue1 to queue2 length-1 times, which will leave only the last element in queue1
                self.queue2.append(self.queue1.popleft())
            self.currQueue = 2 # queue2 now holds our elements
            result = self.queue1.pop() #Save and delete the remaining element in queue1, which is the top of the stack
            self.queue2.append(result) #Append this result to queue2 since we don't want to delete it
            return result
        else:
            for _ in range(self.length - 1):
                self.queue1.append(self.queue2.popleft())
            self.currQueue = 1
            result = self.queue2.pop()
            self.queue1.append(result)
            return result
        

    def empty(self) -> bool:
        return self.length == 0



#Single queue approach
#Takes advantage of the fact that dequeueing and then enqueueing elements repeatedly rotates the queue
#If you dequeue and enqueue n-1 times, you've rotated the queue such that was originally rightmost is now leftmost, which is the top of the virtual stack.
#Furthermore, once you dequeue/enqueue n-1 times, the relative order of the elements will remain the same since we're performing rotation. Therefore, if you
#pop the leftmost value after rotation the rest of the queue will be in its original order
#O(1) complexity for push, O(n) complexity for pop and top
class MyStack2:

    def __init__(self):
        self.queue = deque()
        self.length = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.length += 1

    def pop(self) -> int:
        for _ in range(self.length - 1):
            element = self.queue.popleft()
            self.queue.append(element)
        poppedVal = self.queue.popleft()
        self.length -= 1
        return poppedVal
    
    #For top(), we first rotate n-1 times to save the top of the stack. Then we rotate one last time to get the original queue back
    #So we perform a total of n rotations and restore the queue to its original form
    def top(self) -> int:
        topVal = 0
        for _ in range(self.length - 1):
            element = self.queue.popleft()
            self.queue.append(element)
        topVal = self.queue.popleft()
        self.queue.append(topVal)
        return topVal
        

    def empty(self) -> bool:
        return self.length == 0




#Does NOT work!
#Wrote this single queue approch with the mistaken belief that you can reverse a queue by dequeueing an element and immediately enqueueing it repeatedly
#Doing that only ROTATES the queue, it does not reverse it!!
class MyStackWrong:

    def __init__(self):
        self.queue = deque()
        self.length = 0
        self.reversed = False

    def push(self, x: int) -> None:
        if not self.reversed: #queue is not in reverse order
            self.queue.append(x)

        else: #queue is in reverse order
            for _ in range(self.length - 1):
                element = self.queue.popleft()
                self.queue.append(element)
            self.reversed = False #queue is no longer in reverse order
            self.queue.append(x)

        self.length += 1

    def pop(self) -> int:
        poppedVal = 0
        if not self.reversed: #queue is not in reverse order
            for _ in range(self.length - 1):
                element = self.queue.popleft()
                self.queue.append(element)
            self.reversed = True #queue is now reversed
            poppedVal = self.queue.popleft()
        else:
            poppedVal = self.queue.popleft()
        self.length -= 1
        return poppedVal
        
    def top(self) -> int:
        if self.reversed: #queue is already reversed
            return self.queue[0]
        else: #if queue is not reversed
            for _ in range(self.length - 1):
                element = self.queue.popleft()
                self.queue.append(element)
            self.reversed = True #queue is now reversed
            return self.queue[0]
        

    def empty(self) -> bool:
        return self.length == 0
    




def main():
    print('No test case')
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method