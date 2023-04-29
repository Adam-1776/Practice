#https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    #Binary Search Solution
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        #Helper method to find number of days it will take with a given capacity
        def checkCapacity(capacity: int) -> bool:
            numDays = 1 #Initialize this to one, since it will take at least one day in any case
            currWeight = 0 #Amount of weight we're carrying in the current day
            for weight in weights: #Iterate over the packages one by one. Variable weight is the current package
                if currWeight + weight <= capacity: #We can add this package to the current day's load
                    currWeight += weight
                else: #We cannot add the this package to the current day's load since the capacity would be breached!
                    numDays += 1 #The previous day is finished, start a new day
                    #Below line is important, if the numDays exceeds our limit OR
                    #this package exceeds our capacity (meaning this package cannot be transported)
                    #Then return False since this capacity is not satisfactory
                    if numDays > days or weight > capacity : return False
                    currWeight = weight #We have started a new day starting with the current package
            return True

        #Binary search, need to find the minimum capacity such that checkCapacity(capacity) returns True
        left, right = 1, sum(weights) #Capacity must be at least one, and need not be more than the sum of weights
        while left < right:
            mid = left + (right - left) // 2
            if checkCapacity(mid):
                right = mid
            else:
                left = mid + 1
        return left

def main():
    solution = Solution()
    print(solution.shipWithinDays([1,2,3,4,5,6,7,8,9,10],5))

if __name__ == "__main__": #Entry point
    main() #Calling main method