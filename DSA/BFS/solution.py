from collections import deque

class Solution:
    #Barebones implementation, does not keep track of visited nodes and is prone to cycles and nodes with multiple incoming connections
    #Also, this implementation should not be used to find the minimum distance from one node to another if a node can have multiple univisited neighbors
    #In such graphs, the traversal is done correctly but it does not count distance correctly from root to target node
    def bfs(self, graph: dict[str, list]) -> list[str]:
        output = [] #Store the bfs traversal order
        steps = 0
        queue = deque()
        queue.append('5') #Append root node
        while queue:
            currNode = queue.popleft()
            if currNode == '8': #If we found our target node...
                print(f'distance from 5 to 8 is {steps}')
            output.append(currNode)
            for node in graph[currNode]: #Iterate over neighbors of currNode
                queue.append(node)
            steps += 1
        return output
    
    #This implementation keeps track of visited nodes using a set, so it avoids cycles
    #Also, this implementation should not be used to find the minimum distance from one node to another if a node can have multiple univisited neighbors
    #In such graphs, the traversal is done correctly but it does not count distance correctly from root to target node
    def bfs2(self, graph: dict[str, list]) -> list[str]:
        output = [] #Store the bfs traversal order
        steps = 0
        queue = deque()
        visited = set()
        queue.append('5') #Append root node
        visited.add('5') #Add root node
        while queue:
            currNode = queue.popleft()
            output.append(currNode)
            if currNode == '8': #If we found our target node...
                print(f'distance from 5 to 8 is {steps}')
            for node in graph[currNode]: #Iterate over neighbors of currNode
                if node not in visited:
                    queue.append(node)
                    visited.add(node)
            steps += 1
        return output
    
    #This implementation is compatible with graphs where a dequeued node may have multiple unvisited neighbors. It counts the distance from root to
    #target correctly. Instead of counting the steps of the overall traversal, we keep track of the steps take to reach each individual node.
    def bfs3(self, graph: dict[str, list]) -> list[str]:
        output = [] #Store the bfs traversal order
        queue = deque()
        visited = set()
        queue.append(['5', 0]) #Append root node and the fact that it took zero steps to reach it
        visited.add('5') #Add root node
        while queue:
            currNode = queue.popleft() #currNode is a list [nodeName, stepsFromRoot]
            output.append(currNode[0])
            if currNode[0] == '8': #If we found our target node...
                print(f'distance from 5 to 8 is {currNode[1]}')
            for node in graph[currNode[0]]: #Iterate over neighbors of currNode
                if node not in visited:
                    queue.append([node, currNode[1]+1])
                    visited.add(node)
        return output
    
    #This implementation is also compatible with graphs where a dequeued node may have multiple unvisited neighbors. It counts the distance from root to
    #target correctly. We use an extra loop to count the number of steps correctly.
    def bfs4(self, graph: dict[str, list]) -> list[str]:
        output = [] #Store the bfs traversal order
        steps = 0
        queue = deque()
        visited = set()
        queue.append('5') #Append root node
        visited.add('5') #Add root node
        while queue:
            #We add this extra for loop because each node we encounter has multiple unvisited neighbors
            #this way, we pop the queue the number of times nodes were added to the queue in the previous level 'layer' of exploration
            #Need to do it this way to get an accurate count of numSteps, which is supposed to be the number of 'layers' of exploration
            for _ in range(len(queue)):
                currNode = queue.popleft()
                output.append(currNode)
                if currNode == '8': #If we found our target node...
                    print(f'distance from 5 to 8 is {steps}')
                for node in graph[currNode]: #Iterate over neighbors of currNode
                    if node not in visited:
                        queue.append(node)
                        visited.add(node)
            steps += 1
        return output
    

    #This implementation also allows you to see the path from root to target along with the distance. Since we're storing the full path
    #to encounter each node, we naturally also have the distance from root to each node. It works fine in graphs where a node has multiple
    #unvisited neighbor nodes.
    #This looks tricky but is simple once you understand it. Basically, we are not holding individual nodes in the queue
    #We are holding the entire path in list form that it took to reach the last node in that path. We append and dequeue on this basis.
    #The first time we encounter the target value, we know it's the shortest path, and we already have the path recorded.
    #The algorithm is literally the same as any other BFS, only difference is that we queue the entire path instead of invidual nodes.
    #We simply take the end of the current path as our current node (obviously). We no longer need the steps variable since the lenght of the path
    #list tells us the length of the path to reach the target. This works well but it takes a lot of memory since we store a lot of redundant lists.
    def bfs5(self, graph: dict[str, list]) -> list[str]:
        output = [] #Store the bfs traversal order
        queue = deque()
        visited = set() #Note: visited only stores address of a node, not the entire path list that's in the queue
        queue.append(['5']) #Append path so far (just the root node for now). Note that queue now contains lists, not individual nodes.
        while queue:
            path = queue.popleft() #Current path
            currNode = path[-1] #Current node is at the end of the current path
            if currNode == '8': #If we find the target node, its path is already available
                print(f'Distance between 5 and 8 is {len(path) - 1} and the path is {path}')
            output.append(currNode) #Record current node in normal traversal list
            visited.add(currNode) #Keep track of visitors
            for node in graph[currNode]: #Iterate over neighbors of currNode
                if node not in visited:
                    #Below line is key! We generate the full path to reach 'node' by appending 'node' to the current path
                    #We have to generate a brand new list that ends with 'node', and we append it to our queue
                    updated_path = list(path); updated_path.append(node)
                    visited.add(node)
                    queue.append(updated_path)
        return output
    
    
    #An alternate method to trace the path to go from root to target is to have a dictionary where the key is a node, and its value is its parent
    #Then once you find the target node, you can use your dictionary to trace back the parents going back to the root node. This is memory efficient but
    #is difficult if a node has multiple incoming paths (i.e. a node has multiple parents)



def main():
    #graph image: https://favtutor.com/resources/images/uploads/mceu_10156064211607848109563.jpg
    graph = { #dictionary acting as adjacency list. We will treat node 5 as our root node to start with
    '5' : ['3','7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
    }
    solution = Solution()
    #print(solution.bfs(graph)) # ['5', '3', '7', '2', '4', '8', '8'] distance = 5 and 6 since we visited node 8 twice from different routes
    #print(solution.bfs2(graph)) # ['5', '3', '7', '2', '4', '8'] distance = 5
    #NOTE: both the distances above from nodes 5 to 8 are incorrect!! Since those implementations don't calculate distance correctly when
    # a node can have multiple unvisited neighbors. They do traversal correctly, however.

    #The implementations below show the correct distance since they count distance correctly when a dequeued node may have multiple unvisited neighbors
    #print(solution.bfs3(graph)) # ['5', '3', '7', '2', '4', '8'] distance = 2
    #print(solution.bfs4(graph)) # ['5', '3', '7', '2', '4', '8'] distance = 2
    print(solution.bfs5(graph)) # Distance between 5 and 8 is 2 and the path is ['5', '7', '8'] traversal = ['5', '3', '7', '2', '4', '8']

if __name__ == "__main__": #Entry point
    main() #Calling main method