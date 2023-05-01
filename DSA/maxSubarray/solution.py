#https://leetcode.com/problems/maximum-subarray/

class Solution:
    #Brute force approach
    def maxSubArray(self, nums: list[int]) -> int:
        largestSum = -999999999
        currSum = 0
        latestIncrease = -1
        left, right, = 0, 0
        #Compute all possible subarrays
        for left in range(0, len(nums)):
            currSum = 0 #About to compute all subarrays that start with variable left, reset currSum
            for right in range(left, len(nums)):
                #Since we are computing subarray sums starting from left and moving right one-by-one, we can simply add the
                #current right pointer to our current subarray sum. We can do this since the left pointer is not moving in this loop
                currSum += nums[right]
                if currSum > largestSum : largestSum = currSum #Update the largest subarray sum so far
        return largestSum

def main():
    solution = Solution()
    list1 = [-2,1,-3,4,-1,2,1,-5,4]
    print(solution.maxSubArray(list1)) # 6

if __name__ == "__main__": #Entry point
    main() #Calling main method