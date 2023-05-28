
class Solution:
    
    #Basic recursive template of DFS. No need to manually use a stack since recursion implicitly uses the call stack
    #As you can see, in DFS we continuously search deeper and deeper on the first unvisited neighbor we encounter for each node
    def dfs(self, graph: dict[str, list]) -> list[str]:

        def getNeighbors(currNode: str) -> list[str]: #Helper method to get the neighbors of a node
            return graph[currNode]
        
        visited = set() #We don't re-visit nodes in this implementation
        output = [] #Record the order in which we traverse the nodes in this list

        def dfsRecursive(currRoot: str, target: str, visited:set):
            if currRoot == target: #If we only want to traverse, can omit the functionality to check for target
                print(f'Found the target {target}!')
            output.append(currRoot) #Record the order in which we have visited nodes
            for neighbor in getNeighbors(currRoot): #Like BFS, we get the neighbors of the current node
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfsRecursive(neighbor, target, visited) #Recurse on this neighbor. Notice we we will continuously recurse on the first unvisited neighbor

        visited.add("5")
        dfsRecursive("5", "8", visited) #If we only want to traverse, specifying a target is optional
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
    #print(solution.bfs2(graph)) # ['5', '3', '7', '2', '4', '8'] distance = 5
    #NOTE: both the distances above from nodes 5 to 8 are incorrect!! Since those implementations don't calculate distance correctly when
    # a node can have multiple unvisited neighbors. They do traversal correctly, however.

    #The implementations below show the correct distance since they count distance correctly when a dequeued node may have multiple unvisited neighbors
    #print(solution.bfs3(graph)) # ['5', '3', '7', '2', '4', '8'] distance = 2
    #print(solution.bfs4(graph)) # ['5', '3', '7', '2', '4', '8'] distance = 2
    #print(solution.bfs5(graph)) # Distance between 5 and 8 is 2 and the path is ['5', '7', '8'] traversal = ['5', '3', '7', '2', '4', '8']

if __name__ == "__main__": #Entry point
    main() #Calling main method