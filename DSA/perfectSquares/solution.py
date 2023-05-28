#https://leetcode.com/problems/perfect-squares/

from collections import deque
import math

class Solution:
    #BFS solution. Faster solutions likely exist that use approaches other than BFS, may need to revisit this problem.
    def numSquares(self, n: int) -> int:

        #Helper method to get the list of neighbors for a given node
        def getNeighbors(sum: int) -> list[int]:
            neighbors = []
            maxRange = int(math.sqrt(n)) #We will limit the perfect squares to be subtracted depending on n for efficiency
            for i in range(1, maxRange + 1):
                neighbors.append(sum - (i * i)) #Subtract a perfect square from the current node to find its neighbors
            return neighbors

        #Visualize this as a graph where the root node is n, and we want to reach node 0
        #For a given node, its neighbors are nodes that can be reached by subtracting a perfect square
        #Use BFS to find the shortest route from node n to node 0
        #We enqueue a list consisting of the current node, and the length of the path it took to reach this node from the root
        queue = deque()
        queue.append([n, 0]) #[Current node, number of perfect squares involved in the sum (i.e. length of path to reach this node)]
        visited = set()
        visited.add(n) #We have visited node n
        while queue: #Just a standard BFS traversal
            currNode = queue.popleft()
            if currNode[0] == 0: #If we have found node 0...
                return currNode[1] #We've already computed the length of the path it took to reach this node
            neighbors = getNeighbors(currNode[0]) #Get all the neighbors of currNode
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append([neighbor, currNode[1] + 1]) #We have enqueued a neighbor, the length of the path increases by one
                    visited.add(neighbor)
    
        return 0 #This should be reached since the problem statement assures us that a sum of perfect squares exists for n


def main():
    solution = Solution()
    print(solution.numSquares(12))
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method