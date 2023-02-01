#https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        #We know that numbers from 0 upto and including len(nums) can be in the list. 
        numSet = set(range(0,len(nums)+1)) #We add one to the second paramter to make sure len(nums) is included
        for n in nums:
            numSet.discard(n)
        return numSet.pop() #The only digit left is the answer


def main():
    solution = Solution()
    print(solution.missingNumber([2,1,3])) #0

if __name__ == "__main__": #Entry point
    main() #Calling main method