#https://leetcode.com/problems/maximum-subarray/

class Solution:
    #Fast approach using Kadale's algorithm / Sliding window
    #The trick is to know that the max subarray must have a positive start. It will not start with a negative value
    #or a starting subarray with a negative value. Note: If the entire subarray is full of negative integers then the subarray
    #is simply the biggest integer, this code handles that case also.
    def maxSubArray(self, nums: list[int]) -> int:
        largestSum = -999999999
        largestSubArray = [0,0] #Left and right index that comprises the maximum subarray
        #Using a left pointer is optional and only needed if we want to record the indices of the max subarray
        left, right, = 0, 0
        currSum = 0 #Sum of the subarray we are currently assessing
        while right < len(nums) and left < len(nums): #Keep going until either pointer reaches the end
            currSum += nums[right] #Stretch the current subarray one step to the right
            if currSum > largestSum: #Found a biggest subarray!
                largestSum = currSum
                largestSubArray = [left,right]
            if currSum < 0: #Our current subarray is negative, so we know it is not a start of the maximum subarray. We know this since
                #the maximum subarray must have a positive start. The maximum subarray cannot start with a negative value/subarray, since it
                #would be better to just discard such a starting value/subarray.
                left = right + 1 #Move the left pointer in front of the right pointer, since everything upto and including the right pointer
                #is not part of the maximum subarray
                currSum = 0
            right += 1
        print(f'The largest subarray is from index {largestSubArray[0]} to {largestSubArray[1]} with sum {largestSum}')
        return largestSum



    #Very concise sliding window implementation. This does not keep track of indexes however
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums: return 0
        largestSum = nums[0]
        currentSum = nums[0] #Start off largestSum and currentSum at index 0
        #Iterate over the rest of the list starting at index 1
        for i in range(1, len(nums)):
            currentSum = max(nums[i], currentSum+nums[i]) #Ditch the current window and start a new window at index i if that would give us a higher currentSum
            largestSum = max(largestSum, currentSum) #Keep track of the highest currentSum found
        return largestSum
    


    #Brute force approach
    def maxSubArray2(self, nums: list[int]) -> int:
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