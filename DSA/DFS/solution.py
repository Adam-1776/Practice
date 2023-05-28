
class Solution:
    
    #Basic recursive template of DFS. No need to manually use a stack since recursion implicitly uses the call stack
    #As you can see, in DFS we continuously search deeper and deeper on the first unvisited neighbor we encounter for each node
    #While this can optionally be used to find a target node, it is not guaranteed to be the shortest path and we don't store
    #the path or the length of the path anyway in this template.
    def dfs(self, graph: dict[str, list]) -> list[str]:

        def getNeighbors(currNode: str) -> list[str]: #Helper method to get the neighbors of a node
            return graph[currNode]
        
        visited = set() #We don't re-visit nodes in this implementation
        output = [] #Record the order in which we traverse the nodes in this list

        def dfsRecursive(currRoot: str, target: str, visited:set):
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
    #While this can optionally be used to find a target node, it is not guaranteed to be the shortest path and we don't store
    #the path or the length of the path anyway in this template.
    def dfs2(self, graph: dict[str, list]) -> list[str]:

        def getNeighbors(currNode: str) -> list[str]: #Helper method to get the neighbors of a node
            return graph[currNode]
        
        visited = set() #We don't re-visit nodes in this implementation
        stack = [] #We use this list as a stack to store the order in which we will visit unvisited nodes
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
    print(solution.dfs(graph)) # ['5', '3', '2', '4', '8', '7'] We only visit 8 once, since we don't re-visit any node
    print(solution.dfs2(graph)) # ['5', '7', '8', '3', '4', '2'] this is also a valid DFS traversal. We only visit 8 once, since we don't re-visit any node

    #The implementations below show the correct distance since they count distance correctly when a dequeued node may have multiple unvisited neighbors
    #print(solution.bfs3(graph)) # ['5', '3', '7', '2', '4', '8'] distance = 2
    #print(solution.bfs4(graph)) # ['5', '3', '7', '2', '4', '8'] distance = 2
    #print(solution.bfs5(graph)) # Distance between 5 and 8 is 2 and the path is ['5', '7', '8'] traversal = ['5', '3', '7', '2', '4', '8']

if __name__ == "__main__": #Entry point
    main() #Calling main method