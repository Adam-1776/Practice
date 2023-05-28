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
    

    #Alternate approach using non-recursive DFS. Also, our helper method both finds neighbors and checks if it is land.
    def numIslands2(self, grid: list[list[str]]) -> int:

        numRows, numColumns = len(grid), len(grid[0])
        visited = set()

        def getLandNeighbors(coordinates: tuple) -> list[tuple]: #Helper method to return list of neighboring land coordinates
            row, col = coordinates[0], coordinates[1]
            landNeighbors = []
            if (row + 1) < numRows and grid[row+1][col] == "1":
                landNeighbors.append((row+1, col))
            if (row - 1) >= 0 and grid[row-1][col] == "1":
                landNeighbors.append((row-1, col))
            if (col + 1) < numColumns and grid[row][col+1] == "1":
                landNeighbors.append((row, col+1))
            if (col - 1) >= 0 and grid[row][col-1] == "1":
                landNeighbors.append((row, col-1))
            return landNeighbors


        def dfs(coordinates: tuple):
            stack = []
            stack.append(coordinates) #Append tuple (row, col)
            visited.add(coordinates) #Add this coordinate to our visited set
            while stack:
                currNode = stack.pop()
                neighbors = getLandNeighbors(currNode)
                for neighbor in neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
            
        
        numIslands = 0
        for row in range(numRows):
            for column in range(numColumns):
                currValue = grid[row][column]
                if currValue == "1" and (row, column) not in visited:
                    dfs((row,column)) #Pass a tuple
                    numIslands += 1
        return numIslands

    
    #Simpler approach using recursive DFS. It is easier to validate neighbors this way.
    def numIslands3(self, grid: list[list[str]]) -> int:

        numRows, numColumns = len(grid), len(grid[0])
        visited = set()

        def dfs(coordinates: tuple):
            row, col = coordinates[0], coordinates[1]
            if row < 0 or row >= numRows or col < 0 or col >= numColumns:
                return #We are out of bounds and therefore in water
            if grid[row][col] != "1":
                return #We are not on land, so return
            visited.add(coordinates) #Add this coordinate to our visited set
            neighbors = [(row-1, col), (row+1, col), (row, col+1), (row, col-1)]
            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs(neighbor)
            
        
        numIslands = 0
        for row in range(numRows):
            for column in range(numColumns):
                currValue = grid[row][column]
                if currValue == "1" and (row, column) not in visited:
                    dfs((row,column)) #Pass a tuple
                    numIslands += 1
        return numIslands
    
    
    #Even simpler solution, mark the grid directly instead of a seperate set.
    #Use recursion instead of BFS to traverse outwards from each unvisited land node
    #This recursive approach ends up behaving like DFS, which makes sense since recursion and DFS both use stacks
    #It doesn't matter for this problem whether we use BFS/DFS/recursion since our goal is simply to discover all nodes
    #in the island and the order in which we discover thme doesn't matter
    #Here, we mark a node as "2" to indicate it's been visited and is part of an already discovered island
    def numIslands4(self, grid: list[list[str]]) -> int:
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
    print(solution.numIslands2(grid)) #3
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method