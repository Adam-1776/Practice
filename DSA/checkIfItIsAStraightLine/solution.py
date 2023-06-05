#https://leetcode.com/problems/check-if-it-is-a-straight-line/

from math import inf

#Easy logic, just watch out for edge cases
class Solution:
    #Note that the points do not have to be in order, they can be in any order they just have to form a straight line when connected
    #This code takes care of that since if we encounter a point that is behind the current point, both deltaX and deltaY will be negative
    #so the slope will be positive when we divide them
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        slope = -1 #Slope we've been keeping track of across the points
        for i in range(1,len(coordinates)): #Traverse from index 1 to end, since we continuously compare to the previous index
            deltaY = (coordinates[i][1] - coordinates[i-1][1]) #Change in y axis in this index and the one before it
            deltaX = (coordinates[i][0] - coordinates[i-1][0]) #Change in x axis in this index and the one before it
            if deltaX != 0: #If both x-axis are at different points...
                currSlope = deltaY / deltaX
            elif deltaY == 0: #If both x-axis and y-axis deltas are zero, then this point is a duplicate of the one at the index before it
                continue
            else: #If x-axis delta is zero but y-axis delta is not zero, then the slope is infinite (i.e. pointing straight up)
                currSlope = float(inf)
            if slope == -1: #If this is the first iteration, set the slope variable to the current slope
                slope = currSlope

            if currSlope != slope: #Finally now that we have currSlope and slope, check to make sure they are equal
                return False
        return True #If this line is reached, we never found a non-compliant pair of points



def main():
    solution = Solution()
    coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]

    print(solution.checkStraightLine(coordinates))
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method