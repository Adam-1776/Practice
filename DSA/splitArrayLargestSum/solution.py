#https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    #Binary Search solution
    def splitArray(self, nums: list[int], k: int) -> int:
        #Setting this condition helper method is the key to this problem. It allows us to use Binary Search
        #Basically, this method checks if we can split the array into upto k subarrays, such that the sum of no
        #subarray exceeds subLimit.
        def checkSubArraySum(sumLimit):
            currSum = 0
            numSubArrays = 1
            for num in nums:
                currSum += num
                if currSum > sumLimit:
                    numSubArrays += 1
                    currSum = num
                    if numSubArrays > k : return False
            return True
        
        #Use binary search to find the minimum subLimit that satisfies the condition method, checkSubArraySum()
        left, right = max(nums), sum(nums) #We know the minimum subarray sum in any case has to be the greatest integer in the array (if the size of a subarray is one)
        #And the most it can be is the sum of the entire array (in case there is just one subarray)
        while left < right:
            mid = left + (right - left) // 2
            if checkSubArraySum(mid) :
                right = mid
            else :
                left = mid + 1
        return left

def main():
    solution = Solution()
    print(solution.splitArray([1,2,3,4,5],2))

if __name__ == "__main__": #Entry point
    main() #Calling main method