#https://leetcode.com/problems/move-zeroes/
#This problem is closely related to the 'remove element' leetcode problem

class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0: #If we find a 0 to the left of our right pointer, swap them. This moves the 0 towards the right.
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow] != 0: #Increment the left pointer if it is not pointing to a zero
                slow += 1

    def moveZeroes2(self, nums: list) -> None:
        left = 0
        right = 0
        for right in range(len(nums)):
            nums[left] = nums[right]
            if nums[left] != 0:
                left += 1
        #After the loop above, we have removed all zeroes and preserved order till index left. Now fill zeroes in the remaining indexes
        for i in range(left,len(nums)):
            nums[i] = 0
            

def main():
    solution = Solution()
    list1 = [21,0,0,21,0,37,25,21]
    print(solution.moveZeroes(list1))
    print(list1)

if __name__ == "__main__": #Entry point
    main() #Calling main method