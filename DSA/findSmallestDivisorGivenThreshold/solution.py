#https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

import math

class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        #Does this divisor create a result below or equal to the threshold?
        def checkDivisor(divisor):
            sum = 0
            for num in nums:
                sum += math.ceil(num / divisor) #Divide this way since the quotient is rounded up
                if sum > threshold : return False
            return True

        #classic binary search to find the smallest divisor that fits the criteria
        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if checkDivisor(mid):
                right = mid
            else:
                left = mid + 1
        return left

def main():
    solution = Solution()
    print(solution.smallestDivisor([44,22,33,11,1], 5)) #44

if __name__ == "__main__": #Entry point
    main() #Calling main method