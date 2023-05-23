from collections import deque

#https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        n, m = len(grid[0]), len(grid) #n is horizontal length, m is vertical height
        visited = set() #Hold all the nodes we have visited in tuple form
        numIslands = 0

        def isLand(coordinates: tuple) -> bool: #Helper method to quickly check if a node represented as a tuple is water
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


        for x in range(n):
            for y in range(m):
                if (x,y) not in visited and isLand((x,y)): #We have found a node that's part of an undiscovered island!
                    numIslands += 1
                    bfs(x,y)

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
    print(solution.numIslands(grid))
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method