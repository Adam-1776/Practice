#https://leetcode.com/problems/minimum-absolute-difference

class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        smallestDiff = 99999
        arr.sort() #Sorting the array is the only way to do this efficiently
        solutionList = [] #We use a list, not a set. The fact that we need to keep things in order is a hint to use a list.
        for i in range(1,len(arr)): #Start from index one since we will compare it with the index previous to it. Keep going till the end.
            diff = abs(arr[i]-arr[i-1]) #Absolute difference between these two indexes
            if diff < smallestDiff: #This pair has the smallest difference seen so far
                smallestDiff = diff #Record the new smallest absolute difference
                solutionList.clear() #Clear our solutionList since we've found a new smallest pair
                solutionList.append([arr[i-1],arr[i]]) #Add this new smallest pair
            elif diff == smallestDiff: #New pair with same difference as the smallest difference
                solutionList.append([arr[i-1],arr[i]]) #Append this pair to our list
        
        return solutionList

def main():
    solution = Solution()
    print(solution.minimumAbsDifference([3,8,-10,23,19,-4,-14,27])) #

if __name__ == "__main__": #Entry point
    main() #Calling main method