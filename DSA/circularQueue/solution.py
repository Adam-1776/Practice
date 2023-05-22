#https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/1337/

class MyCircularQueue:

    def __init__(self, k: int):
        print(f'Setting up circular queue with size {k}')
        self.arr = [0] * k
        self.capacity = k
        self.front = 0 #The actual index that holds the front of the queue
        self.back = 0 #The index that is next *available* for enqueueing. This is not the actual index that has the back of the queue!
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size >= self.capacity : return False
        newBack = (self.back + 1) % self.capacity #Move back to the right, loop around the list if we reach the end. This will be the next spot
        #available for enqueuing once we are done with this enqueue
        #self.back is the next available spot to enqueue, so we put the value there
        print(f'Going to enqueue value {value} to arr[{self.back}], newBack is {newBack}')
        self.arr[self.back] = value
        self.back = newBack #Update self.back with newBack we calculated earlier
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size <= 0 : return False
        returnVal = self.Front() #The value we are about to dequeue
        newFront = (self.front + 1) % self.capacity #Calculate the new front once we are done with this dequeue
        #We move the front variable to the right and loop around the list if we reach the end of the list
        print(f'Going to dequeue value {returnVal} from arr[{self.front}], newFront is {newFront}')
        self.front = newFront #Update self.front with the new front we calculated earlier
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty() : return -1
        return self.arr[self.front] #self.front holds the actual index of the frontmost value

    def Rear(self) -> int:
        if self.isEmpty() : return -1
        return self.arr[(self.back-1) % self.capacity] #self.back is the index that comes AFTER the actual back of the queue,
        #so we have to subtract one from self.back to find the actual back. We may have to loop around the list if necessary

    def isEmpty(self) -> bool:
        return self.size <= 0

    def isFull(self) -> bool:
        return self.size >= self.capacity



def main():
    print('No test case available')
    # Your MyCircularQueue object will be instantiated and called as such:
    # obj = MyCircularQueue(k)
    # param_1 = obj.enQueue(value)
    # param_2 = obj.deQueue()
    # param_3 = obj.Front()
    # param_4 = obj.Rear()
    # param_5 = obj.isEmpty()
    # param_6 = obj.isFull()
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method