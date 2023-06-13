#https://leetcode.com/problems/equal-row-and-column-pairs/


from collections import Counter


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:

        #Helper method that returns a tuple containing elements in specified column (zero indexed) from top-to-bottom order
        def getColumn(col):
            column = []
            for i in range(len(grid)):
                column.append(grid[i][col])
            return tuple(column)

        setColumns = Counter() #We use a Counter instead of a set because identical columns may be present, and we want to record how many times each identical column is present
        setRows = Counter() #Use a counter instead of a set for same reason
        #Note: We could have also used defaultdict(int)
        for c in range(len(grid[0])):
            setColumns[getColumn(c)] += 1 #Record each column in the counter. We use a tuple instead of a list to store each column because they will not be modified and it's hashable
        for r in range(len(grid)):
            setRows[tuple(grid[r])] += 1 #Similarly, record each row
        
        #print(f'rows = {setRows}')
        #print(f'columns = {setColumns}')
        counter = 0
        for sequence in setColumns:
            if sequence in setRows: #If we find a row/column that is present both as a row and a column in the matrix...
                counter += setColumns[sequence] * setRows[sequence] #Since we are looking for unique row pair INDEXES, it is okay if the values within each matching sequence are duplicate
                #Therefore, we multiply the number of times this sequence is present as a row by the number of times it's present as a column.
                #If there are r rows with a sequence and c columns with the same sequence, the number of matching pairs = r1,c1 r1,c2 r1,c3 ... r2,c1...rn,cn
                #The total number of pairs will therefore be r * c
        return counter



    #More concise approach, same complexity
    def equalPairs2(self, grid: list[list[int]]) -> int:

        #Helper method that returns a tuple containing elements in specified column (zero indexed) from top-to-bottom order
        def getColumn(col):
            column = []
            for i in range(len(grid)):
                column.append(grid[i][col])
            return tuple(column)

        setColumns = Counter()
        count = 0
        for c in range(len(grid[0])):
            setColumns[getColumn(c)] += 1 
        for r in grid:
            count += setColumns[tuple(r)] #If we find a row that is also present as a column n times, we have just found n more pairs
        return count



def main():
    solution = Solution()
    list1 = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]

    print(solution.equalPairs(list1))
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method