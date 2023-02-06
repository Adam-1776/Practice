#https://leetcode.com/problems/remove-element/

class Solution:
    #We use a two pointer approach to delete the unwatned value in-place
    def removeElement(self, nums: list[int], val: int) -> int:
        l = 0
        r = 0 #Initialize left and right pointers
        #Keep copying the value of the right pointer to the index at the left pointer
        #Only increment the left pointer when we have copied a non-unwanted value
        while r < len(nums):
            nums[l] = nums[r]
            if nums[l] != val:
                l += 1 #If we copy a non-unwanted value, increment the left pointer. Else the left pointer does not get incremented
            r += 1 #We increment the right pointer every time
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