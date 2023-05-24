from collections import deque

#https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        deadendSet = set(deadends)
        numSteps = 0
        queue = deque()
        visited = set()
        queue.append("0000")
        visited.add("0000")

        def getNeighbors(combination: str) -> list[str]: #Helper method to find all the neighbors of a given node
            if combination in deadendSet : return [] #If the node is a deadend, it has no neighbors we can transition to
            neighbors = []
            for place in range(len(combination)): #Increment and decrement each of the four digits one by one to find eight neighbors
                biggerDigit = str((int(combination[place]) + 1) % 10) #Increment the digit at this place
                biggerNode = combination[0:place] + biggerDigit + combination[place+1:]
                neighbors.append(biggerNode)
                lesserDigit = str((int(combination[place]) - 1) % 10) #Decrement the digit at this place
                lesserNode =  combination[0:place] + lesserDigit + combination[place+1:]
                neighbors.append(lesserNode)
            #print(f'neighbors of {combination} are {neighbors}')
            return neighbors

        while queue:
            for _ in range(len(queue)): #We add this extra for loop because each node we encounter has multiple unvisited neighbors
                #this way, we pop the queue the number of times a node was added to the queue in the previous level 'layer' of exploration
                #Need to do it this way to get an accurate count of numSteps, which is supposed to be the number of 'layers' of exploration
                currNode = queue.popleft()
                if currNode == target:
                    return numSteps
                currNeighbors = getNeighbors(currNode)
                for neighbor in currNeighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
                    visited.add(neighbor)
            numSteps += 1
        return -1
    
    #Alternate approach. This time, we simply include the 'depth' of each node alongside the combination
    #So each we enqueue a list in format [combination, numberOfSteps]
    def openLock2(self, deadends: list[str], target: str) -> int:
        deadendSet = set(deadends)
        queue = deque()
        visited = set()
        queue.append(["0000", 0]) #It took zero steps to reach combination 0000, enqueue this
        visited.add("0000")

        def getNeighbors(combination: str) -> list[str]: #Helper method to get neighbors
            if combination in deadendSet : return []
            neighbors = []
            for place in range(len(combination)):
                biggerDigit = str((int(combination[place]) + 1) % 10) #Increment the digit at this place
                biggerNode = combination[0:place] + biggerDigit + combination[place+1:]
                neighbors.append(biggerNode)
                lesserDigit = str((int(combination[place]) - 1) % 10) #Decrement the digit at this place
                lesserNode =  combination[0:place] + lesserDigit + combination[place+1:]
                neighbors.append(lesserNode)
            #print(f'neighbors of {combination} are {neighbors}')
            return neighbors

        while queue:
            currNode = queue.popleft()
            if currNode[0] == target:
                return currNode[1] #We've already stored the number of steps needed to reach this node, so can simply return it
            currNeighbors = getNeighbors(currNode[0])
            for neighbor in currNeighbors:
                if neighbor not in visited:
                    queue.append([neighbor, currNode[1]+1]) #We know neighbor is right next to currNode, so number of steps to reach
                    #this neighbor is exactly one greater than currNode
                visited.add(neighbor)
        return -1

def main():
    deadEnds = ["0201","0101","0102","1212","2002"]
    solution = Solution()
    print(solution.openLock(deadEnds, "0202")) #6
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method