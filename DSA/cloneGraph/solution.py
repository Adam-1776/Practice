#https://leetcode.com/problems/clone-graph/

from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    #BFS approach. We use a dictionary to not only store which nodes have been visited, but also to save the equivalent node in the new graph
    #for each node in the original graph. Then we perform a BFS, creating new Nodes and adding them to the map as appropriate.
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        newRoot = Node(node.val) #Clone the root node
        mapOldtoNew = dict() #Maps old node to its equivalent node in the new graph. This also acts as our visited set
        mapOldtoNew[node] = newRoot #Add the root node
        queue = deque() #Going to do a BFS traversal
        queue.append(node) #Enqueue the original root node
        #Start BFS traversal
        while queue:
            currNode = queue.popleft() #currNode is an original node whose new counterpart is already in the dictionary
            for neighbor in currNode.neighbors:
                if neighbor not in mapOldtoNew: #If we find a neighbor node we haven't seen before...
                    mapOldtoNew[neighbor] = Node(neighbor.val) #Create a corresponding new node for this neighbor and map it
                    queue.append(neighbor) #Enqueue it since this neighbor has never been currNode
                mapOldtoNew[currNode].neighbors.append(mapOldtoNew[neighbor]) #Get the new node equivalent of currNode, and add the new neighbor
        
        return newRoot
    

    #Non recursive DFS approach. We use a dictionary to not only store which nodes have been visited, but also to save the equivalent node in the new graph
    #for each node in the original graph. Then we perform a DFS, creating new Nodes and adding them to the map as appropriate.
    def cloneGraph2(self, node: 'Node') -> 'Node':
        if not node: return node
        newRoot = Node(node.val) #Clone the root node
        mapOldtoNew = dict() #Maps old node to its equivalent node in the new graph. This also acts as our visited set
        mapOldtoNew[node] = newRoot #Add the root node
        stack = [] #Going to do a BFS traversal
        stack.append(node) #Enqueue the original root node
        #Start DFS traversal
        while stack:
            currNode = stack.pop() #currNode is an original node whose new counterpart is already in the dictionary
            for neighbor in currNode.neighbors:
                if neighbor not in mapOldtoNew: #If we find a neighbor node we haven't seen before...
                    mapOldtoNew[neighbor] = Node(neighbor.val) #Create a corresponding new node for this neighbor and map it
                    stack.append(neighbor) #Push this to stack since this neighbor has never been currNode
                mapOldtoNew[currNode].neighbors.append(mapOldtoNew[neighbor]) #Get the new node equivalent of currNode, and add the new neighbor
        
        return newRoot



def main():
    print(f'No test case available here')
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method