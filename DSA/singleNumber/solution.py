#https://leetcode.com/problems/single-number/


class Solution:
    #O(1) space complexity solution. This works whenever one digit is present an odd number of times, and the others are present an even number of times
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
            

def main():
    solution = Solution()
    nums = [4,1,2,1,2]
    print(solution.singleNumber(nums)) #4

if __name__ == "__main__": #Entry point
    main() #Calling main method