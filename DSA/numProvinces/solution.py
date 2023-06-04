#https://leetcode.com/problems/number-of-provinces/


class Solution:
    #Recursive solution with DFS
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        numProvinces = 0
        visited = set()

        def dfs(city):
            neighbors = isConnected[city] #Get list of all potential neighbors of this city
            for i in range(n): #We know the length of potential neighbors is n
                if i not in visited and neighbors[i] == 1: #Remember, the index identifies the node, not the values inside neighbors list!
                    visited.add(i)
                    dfs(i)

        for city in range(n): #Important: The index itself is the name, or identifier of each node
            if city not in visited:
                visited.add(city) #Found an unvisited city
                dfs(city) #Mark all cities connected to this city, thus completing the province it is in
                numProvinces += 1
        return numProvinces
    

    #Non-recursive solution, uses DFS with stack.
    def findCircleNum2(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        numProvinces = 0
        visited = set()

        def dfs(city):
            stack = []
            stack.append(city)
            while stack:
                city = stack.pop()
                neighbors = isConnected[city]
                for i in range(n):
                    if i not in visited and neighbors[i] == 1:
                        visited.add(i)
                        stack.append(i)

        for city in range(n):
            if city not in visited:
                visited.add(city)
                dfs(city)
                numProvinces += 1
        return numProvinces


#Note, this problem is logically almost the same as the number of islands problem. Basically we need to find the number of unconnected portions in the graph
def main():
    solution = Solution()
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]

    print(solution.findCircleNum(isConnected))
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method