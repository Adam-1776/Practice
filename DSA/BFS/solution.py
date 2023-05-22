from collections import deque

class Solution:
    #Barebones implementation, does not keep track of visited nodes and is prone to cycles and nodes with multiple incoming connections
    def bfs(self, graph: dict[str, list]) -> list[str]:
        output = [] #Store the bfs traversal order
        steps = 0
        queue = deque()
        queue.append('5') #Append root node
        while queue:
            currNode = queue.popleft()
            output.append(currNode)
            for node in graph[currNode]:
                queue.append(node)
                if node == '8': #If we found our target node...
                    print(f'distance from 5 to 8 is {steps}')
            steps += 1
        return output
    
    #This implementation keeps track of visited nodes using a set, so it avoids cycles
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
            for node in graph[currNode]:
                if node not in visited:
                    queue.append(node)
                    visited.add(node)
                    if node == '8': #If we found our target node...
                        print(f'distance from 5 to 8 is {steps}')
            steps += 1
        return output

    #This implementation also allows you to see the path from root to target along with the distance
    #This looks tricky but is simple once you understand it. Basically, we are not holding individual nodes in the queue
    #We are holding the entire path in list form that it took to reach the last node in that path. We append and dequeue on this basis.
    #The first time we encounter the target value, we know it's the shortest path, and we already have the path recorded.
    #The algorithm is literally the same as any other BFS, only difference is that we queue the entire path instead of invidual nodes.
    #We simply take the end of the current path as our current node (obviously). We no longer need the steps variable since the lenght of the path
    #list tells us the length of the path to reach the target. This works well but it takes a lot of memory since we store a lot of redundant lists.
    def bfs3(self, graph: dict[str, list]) -> list[str]:
        output = [] #Store the bfs traversal order
        queue = deque()
        visited = set()
        queue.append(['5']) #Append path so far (just the root node for now). Note that queue now contains lists, not individual nodes.
        while queue:
            path = queue.popleft() #Current path
            currNode = path[-1] #Current node is at the end of the current path
            if currNode == '8': #If we find the target node, its path is already available
                print(f'Distance between 5 and 8 is {len(path) - 1} and the path is {path}')
            output.append(currNode) #Record current node in normal traversal list
            visited.add(currNode) #Keep track of visitors
            for node in graph[currNode]:
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
    #print(solution.bfs(graph)) # ['5', '3', '7', '2', '4', '8', '8']
    #print(solution.bfs2(graph)) # ['5', '3', '7', '2', '4', '8']
    print(solution.bfs3(graph)) # Distance between 5 and 8 is 2 and the path is ['5', '7', '8'] traversal = ['5', '3', '7', '2', '4', '8']

if __name__ == "__main__": #Entry point
    main() #Calling main method