#https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/


class Solution:
    #Sort the list first and then check all the differences. O(nlog(n)) time complexity, constant space complexity
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2,len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True


    #Solution without sorting. It has linear time complexity
    def canMakeArithmeticProgression2(self, arr: list[int]) -> bool:
        smallest, greatest = min(arr), max(arr)
        diff = (greatest - smallest) / (len(arr) - 1) #Calculate the expected difference between all the nums if they are sorted
        if diff == 0: return True #If diff is 0, then all the values are the same. This is the only case where duplicate values are allowed
        if not diff.is_integer(): return False #if diff is not a whole number, then it's not an arithmetic progression
        else: diff = int(diff)
        setNums = {smallest + (diff * i) for i in range(len(arr))} #Create a set with all the nums expected to be in arr. We use set comprehension here
        for i in range(len(arr)):
            try:
                setNums.remove(arr[i]) #Attempt to remove arr[i] from our set
            except:
                return False #If an exception is thrown due to arr[i] not being in the set, then it's not an arithmetic sequence and we can return False

        return True


def main():
    solution = Solution()
    list1 = [3,5,1]

    print(solution.canMakeArithmeticProgression(list1))
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method