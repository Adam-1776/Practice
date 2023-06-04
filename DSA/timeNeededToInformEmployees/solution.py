#https://leetcode.com/problems/time-needed-to-inform-all-employees/


from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        #First, generate an adjacency list showing who the subordinates are for each manager.
        #Employees with no subordinates are not needed as keys in this dictionary, since they are leaf nodes and we do not to traverse below them.
        subordinates = defaultdict(list)
        for i in range(n): #Iterate over each employee ID at a time and find out who their manager is
            if i != headID: #head of company does not have a manager
                subordinates[manager[i]].append(i) #Record that manager[i] has subordinate i
        #Subordinates is now a dictionary where key is manager ID, and value is list of direct reports. It serves as an adjacency list

        maxTime = 0 #Longest time we've discovered to contact an employee

        def dfs(currNode, timeTaken): #Current employee, time taken for current employee to receive news
            nonlocal maxTime
            maxTime = max(maxTime, timeTaken)
            neighbors = subordinates[currNode] #If an employee has no subordinates, an empty list is returned. So no null nodes will be recursed
            for employee in neighbors:
                dfs(employee, timeTaken + informTime[currNode]) #Time for a subordinate to receive news is timeTaken for currNode + time taken for currNode to inform the subordinate

        dfs(headID, 0) #The head of the company has the information at time = 0
        return maxTime



def main():
    solution = Solution()
    manager = [2,2,-1,2,2,2]
    informTime = [0,0,1,0,0,0]

    print(solution.numOfMinutes(6,2,manager,informTime))
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method