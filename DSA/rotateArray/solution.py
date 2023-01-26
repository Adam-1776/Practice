#https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: list[int], k: int) -> None: #Not returning anything, since we'll modify it in-place
        solutionList = [0] * len(nums)
        for i in range(0,len(nums)):
            newIndex = (i+k) % len(nums)
            solutionList[newIndex] = nums[i]
        for i in range(0,len(nums)):
            nums[i] = solutionList[i]


def main():
    solution = Solution()
    list1 = [1,2,3,4,5,6,7]
    solution.rotate(list1, 3)
    print(list1) #[5,6,7,1,2,3,4]

if __name__ == "__main__": #Entry point
    main() #Calling main method