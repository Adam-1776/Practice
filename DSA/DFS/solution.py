
class Solution:
    
    #Basic recursive template of DFS. No need to manually use a stack since recursion implicitly uses the call stack
    #As you can see, in DFS we continuously search deeper and deeper on the first unvisited neighbor we encounter for each node
    #While this can optionally be used to find a target node, it is not guaranteed to be found in the shortest path and we don't store
    #the path or the length of the path anyway in this template.
    def dfs(self, graph: dict[str, list]) -> list[str]:

        def getNeighbors(currNode: str) -> list[str]: #Helper method to get the neighbors of a node
            return graph[currNode]
        
        visited = set() #We don't re-visit nodes in this implementation
        output = [] #Record the order in which we traverse the nodes in this list (not needed in most leetcode problems)

        def dfsRecursive(currRoot: str, target: str, visited:set): #Adding target and visited is optional here since this is a python helper function
            if currRoot == target: #If we only want to traverse, can omit the functionality to check for target
                print(f'Found the target {target}!')
            output.append(currRoot) #Record the order in which we have visited nodes
            neighbors = getNeighbors(currRoot)
            for neighbor in neighbors: #Like BFS, we get the neighbors of the current node
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfsRecursive(neighbor, target, visited) #Recurse on this neighbor. Notice we we will continuously recurse on the first unvisited neighbor

        visited.add("5")
        dfsRecursive("5", "8", visited) #If we only want to traverse, specifying a target is optional
        return output
    

    #Basic non-recursive template of DFS. Same technique as above except we manually use a stack instead of recursion
    #While this can optionally be used to find a target node, it is not guaranteed to be found in the shortest path and we don't store
    #the path or the length of the path anyway in this template.
    def dfs2(self, graph: dict[str, list]) -> list[str]:

        def getNeighbors(currNode: str) -> list[str]: #Helper method to get the neighbors of a node
            return graph[currNode]
        
        visited = set() #We don't re-visit nodes in this implementation
        stack = [] #We use this list as a stack to store the order in which we will visit unvisited nodes (not needed in most leetcode problems)
        output = [] #Record the order in which we traverse the nodes in this lis
        visited.add("5")
        stack.append("5")
        target = "8" #This is optional

        while stack:
            currNode = stack.pop()
            if currNode == target: #Searching for target is optional if we just want to traverse
                print(f'Found the target {target}!')
            output.append(currNode)
            neighbors = getNeighbors(currNode)
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        return output
    
    #Non-recursive template of DFS. This time we store the length it took to reach each node in the given path we took to reach it
    #Important: we don't keep track of visited nodes and can visit a node multiple times to evaluate the shortest path.
    #As a consequence, the same node can be in the stack more than once and this implementation is prone to cycles!
    def dfs3(self, graph: dict[str, list]) -> list[str]:

        def getNeighbors(currNode: str) -> list[str]: #Helper method to get the neighbors of a node
            return graph[currNode]
        
        #This time, we don't keep track of visited nodes since we may need to revisit a node since there may be
        #multiple paths to a node and we need to evaluate them all.
        stack = [] #We use this list as a stack to store the order in which we will visit unvisited nodes. Each element
        #in the stack is a list comprising [node, distanceFromRoot]. Note that the stack may have mutiple entries for each
        #node since we can revisit nodes in this implementation and they may have multiple distanceFromRoot values, since we
        #took different paths to reach that node.
        output = [] #Record the order in which we traverse the nodes in this lis
        stack.append(["5", 0]) #Push the root node and the number of steps to reach it.
        target = "8"
        shortestPath = 99999

        while stack:
            currNode = stack.pop()
            if currNode[0] == target: #currNode[0] is the node we are currently at, and currNode[1] is the distance it took to reach it the current path
                if currNode[1] < shortestPath:
                    shortestPath = currNode[1]
                print(f'Found the target {target}, distance is {currNode[1]}')
            output.append(currNode[0])
            neighbors = getNeighbors(currNode[0])
            for neighbor in neighbors:
                stack.append([neighbor, currNode[1] + 1])

        print(f'Shortest path from root to {target} is {shortestPath}')
        return output
    

    #Non-recursive template of DFS. This time we store the entire path it took to reach each node in the given path we took to reach it
    #Important: we don't keep track of visited nodes and can visit a node multiple times to evaluate the shortest path.
    #As a consequence, the same node can be in the stack more than once and this implementation is prone to cycles!
    def dfs4(self, graph: dict[str, list]) -> list[str]:

        def getNeighbors(currNode: str) -> list[str]: #Helper method to get the neighbors of a node
            return graph[currNode]
        
        #This time, we don't keep track of visited nodes since we may need to revisit a node since there may be
        #multiple paths to a node and we need to evaluate them all. 
        stack = [] #We use this list as a stack to store the order in which we will visit unvisited nodes. Each element
        #in the stack is a list comprising [pathFromRoot]. Note that the stack may have mutiple entries for each
        #node since we can revisit nodes in this implementation and they may have multiple pathFromRoot values, since we
        #took different paths to reach that node.
        output = [] #Record the order in which we traverse the nodes in this lis
        stack.append(["5"]) #Push the path we have explored so far (just the root node for now)
        target = "8"
        shortestPath = []

        while stack:
            currNode = stack.pop()
            if currNode[-1] == target: #Last element in currNode is the node we are currently at
                if not shortestPath or len(shortestPath) > len(currNode): #If shortestPath hasn't been set or we found a new shortest path...
                    shortestPath = currNode
                #print(f'Found the target {target}, path is {currNode}')
            output.append(currNode[-1])
            neighbors = getNeighbors(currNode[-1])
            for neighbor in neighbors:
                stack.append(list(currNode) + [neighbor]) #Append neighbor to the list so far and push it to the stack

        print(f'Shortest path from root to {target} is {shortestPath}')
        return output
        


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
    #print(solution.dfs(graph)) # ['5', '3', '2', '4', '8', '7'] We only visit 8 once, since we don't re-visit any node. This does a left recursion.
    #print(solution.dfs2(graph)) # ['5', '7', '8', '3', '4', '2'] this does right recursion and is also a valid DFS traversal. We only visit 8 once, since we don't re-visit any node

    #The implementations below keeps track of the distance/path from root to the node for the path it's currently on. It can visit a node multiple times.
    #Notice how we visited eight twice. We record the shortest distance/path it took to reach eight each time we encounter it.
    #The below implementations are prone to cycles, however.
    #print(solution.dfs3(graph)) #['5', '7', '8', '3', '4', '8', '2'] distance = 2
    print(solution.dfs4(graph)) #['5', '7', '8', '3', '4', '8', '2'] and shortest path is ['5', '7', '8']

    #As you can see, while it is possible to find the shortest distance or shortest path from root to target using DFS, it can be inefficient since we visit the same
    #node multiple times, and we are prone to cycles. For this reson, it is better to use BFS when we need to find the shortest path from root to target.
    #DFS is still fine for finding a route from root to target when we don't need the shortest route, or we have a graph where we know one path exists between
    #any two nodes (such as a tree)

if __name__ == "__main__": #Entry point
    main() #Calling main method