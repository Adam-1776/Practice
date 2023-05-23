from collections import deque

#https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        n, m = len(grid[0]), len(grid) #n is horizontal length, m is vertical height
        visited = set() #Hold all the nodes we have visited in tuple form
        numIslands = 0

        def isLand(coordinates: tuple) -> bool: #Helper method to quickly check if a node represented as a tuple is land
            x, y = coordinates[0], coordinates[1]
            if x < 0 or x >= n: #x out of bounds
                print(f'Coordinates [{x}][{y}] is water')
                return False
            if y < 0 or y >= m: #y out of bounds
                print(f'Coordinates [{x}][{y}] is water')
                return False
            if grid[y][x] == "0": #Have to it this way since grid is stuctured as each horizontal line as a list element,
                #so the first index in grid is the vertical coordinate, and the second coordinate is horizontal
                print(f'Coordinates [{x}][{y}] is water')
                return False
            else:
                print(f'Coordinates [{x}][{y}] is land')
                return True

        def bfs(xCoordinate: int, yCoordinate: int):
            queue = deque()
            queue.append((xCoordinate,yCoordinate))
            visited.add((xCoordinate,yCoordinate))
            while queue:
                currNode = queue.popleft() #CurrNode is now a tuple with x and y coordinates
                x, y = currNode[0], currNode[1] #Get the x and y coordinates as seperate integers for readability
                currNeighbors = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)] #Generate all four neighbors of currNode
                for neighborNode in currNeighbors: #Iterate over neighbors of currNode
                    if (neighborNode not in visited) and isLand(neighborNode): #Found another land node that's part of this island
                        queue.append(neighborNode)
                    visited.add(neighborNode) #Add neighborNode to visited regardless of whether it's land or water
                    #Note: We can also only add neighborNode to visited if it's land, that also works since in our main loop, we only
                    #enter BFS for a node if it's unvisited AND land

        for x in range(n):
            for y in range(m):
                if (x,y) not in visited and isLand((x,y)): #We have found a node that's part of an undiscovered island!
                    numIslands += 1
                    bfs(x,y)
        return numIslands

    #Simpler solution, use recursion instead of BFS to traverse outwards from each unvisited land node
    def numIslands2(self, grid: list[list[str]]) -> int:
        n, m = len(grid[0]), len(grid) #n is horizontal length, m is vertical height
        numIslands = 0

        def exploreIsland(x: int, y: int): #Helper method to recursively mark all nodes belonging to current island
            if x >= m or x < 0 or y >=n or y < 0 : return #Exceeding bounds of grid means water, and thus end of island
            if grid[x][y] == "1": #If this node is an unvisited land node, it must be part of this island
                grid[x][y] = "2" #Mark this node as visited and belonging to an already explored island
                exploreIsland(x+1, y) #Recursively explore each neighbor
                exploreIsland(x-1, y)
                exploreIsland(x, y+1)
                exploreIsland(x, y-1)
            else: #If we hit water, it means we've hit our terminal case since we reached end of island
                return
            
        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1":
                    numIslands += 1
                    exploreIsland(x,y)
        return numIslands

        
    
#The idea is to perform a bfs when we find an unvisited land node. This univisited land node is guaranteed to be part of a new island, since if it was
#part of an existing island it would have already been visited. Then take this unvisited land node and perform bfs to find all the other land nodes that
#belong to this island, marking them as visited. We now have all the land nodes of this island marked as visited. Repeat this process with other unvisited land
#nodes and you will have found all the islandss

def main():
    grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]]
    solution = Solution()
    print(solution.numIslands(grid)) #3
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method