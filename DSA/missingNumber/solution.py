#https://leetcode.com/problems/missing-number/

class Solution:
    #Linear time complexity, linear space complexity
    def missingNumber(self, nums: list[int]) -> int:
        #We know that numbers from 0 upto and including len(nums) can be in the list. 
        numSet = set(range(0,len(nums)+1)) #We add one to the second paramter to make sure len(nums) is included
        for n in nums:
            numSet.discard(n)
        return numSet.pop() #The only digit left is the answer

    #To-do: implement a O(1) space complexity solution using bit manipulation or  Gauss' Formula


def main():
    solution = Solution()
    print(solution.missingNumber([2,1,3])) #0

if __name__ == "__main__": #Entry point
    main() #Calling main method