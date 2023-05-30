#https://leetcode.com/problems/remove-element/

class Solution:
    #We use a two pointer approach to delete the unwanted value in-place. It preserves the relative order of the elements
    def removeElement(self, nums: list[int], val: int) -> int:
        l = 0
        r = 0 #Initialize left and right pointers
        #Keep copying the value of the right pointer to the index at the left pointer
        #Only increment the left pointer when we have copied a non-unwanted value
        while r < len(nums):
            nums[l] = nums[r]
            if nums[l] != val:
                l += 1 #If we copy a good value, increment the left pointer.
            #If we copied a bad value, the left pointer does not get incremented and will be overwritten in the next iteration. (common pattern)
            r += 1 #We increment the right pointer every time
        return l #Return length of new list

    #Alternative solution. It moves the unwanted values to the right of the list. This is equal to the move zeroes problem.
    def removeElement2(self, nums: list[int], val: int) -> int:
        l = 0
        r = 0 #Initialize left and right pointers
        while r < len(nums):
            #print(nums)
            if nums[l] == val and nums[r] != val: #If left is unwanted and right is good, swap them. This moves the unwanted value towards the right
                nums[l],nums[r] = nums[r],nums[l] #Do not increment left pointer if we performed a deletion!
            if nums[l] != val :
                l += 1 #Only increment left pointer if we did not delete anything in this iteration
            r += 1 #We can increment the right pointer every time
        return l #Return length of new list
            

#The approach above us to use one pointer to keep track of which index to copy the next value to. If we copy the unwanted value
#Then we do not increment the left pointer which will cause the unwanted value there to get overwritten.
def main():
    solution = Solution()
    list1 = [21,47,21,21,13,37,25,21]
    print(solution.removeElement(list1,21)) # 4
    print(list1)

if __name__ == "__main__": #Entry point
    main() #Calling main method