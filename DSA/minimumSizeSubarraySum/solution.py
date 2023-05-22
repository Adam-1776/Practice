#https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    #Solve using sliding window approach
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        minLength = 9999999999
        curSum = 0
        left, right = 0,0
        while right < len(nums):
            curSum += nums[right]
            if curSum >= target:
                while curSum >= target:
                    if right - left < minLength: minLength = right - left + 1
                    curSum -= nums[left]
                    left += 1
            right += 1
        if minLength == 9999999999 : return 0
        else: return minLength

         
#Sliding window approach. Keep incrementing the right pointer till the condition is met. When that happens, increment the left pointer till the condition is no longer met.

def main():
    solution = Solution()
    print(solution.minSubArrayLen(7, [2,3,1,2,4,3])) #2

if __name__ == "__main__": #Entry point
    main() #Calling main method