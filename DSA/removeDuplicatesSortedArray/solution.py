#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    
    #Inefficient solution, does not take advantage of the fact that we don't have to shrink the list
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) < 2 : return
        i = 0
        while True :
            if i >= len(nums) - 1 or len(nums) < 2 : return #Return if there's one element left or we'e reached the end of the list
            if nums[i] == nums[i+1]: #If the next index has a dupliate element, delete it
                del nums[i+1]
                i -= 1 #We want to stay at our current index to see if we have more duplicates ahead. We decrement here so it cancels the upcoming increment.
            i += 1

    #Efficient solution. Take advantage of the fact that we don't have to shrink the list, and that non-unique values must be consecutively placed
    #We use two pointers: one pointer to record where the next new number will go, and the other pointer to discover new integers.
    def removeDuplicates2(self, nums: list[int]) -> int:
        if len(nums) < 2 : return
        #nonUnique is basically the next index where a unique integer will go. The list upto index nonUnique is guaranteed to be unique at all times.
        #So we're basically splitting the list in two. All indexes before nonUnique must be unique, all indexes from nonUnique onwards may not
        nonUnique = 1 #Start this at 1 because we know we won't move the first integer, and the second unique integer must go to index 1
        index = 1
        numRemoved = 0 #Use this counter to get the number of unique elements after all the deletions.
        #The key idea is that, we detect a duplicate integer if the index before it has the same value
        #Therefore, if we encounter an integer that does not have the same value as its previous index, we must have encountered this integer for the first time
        #This doesn't mean that integer is necessarily unique because it could have a duplicate value to its right, but since we're encountering it for the
        #first time, we add it to the next available opening in our list. 
        while index < len(nums) :
            if nums[index] == nums[index-1] : #If the numbers at the current index and the index before are the same ...
                numRemoved += 1 #We found another duplicate, increment this.
            else: #If the numbers at the current index and the previous index are unique, the current index is a number we're seeing for the first time ...
                nums[nonUnique] = nums[index] #Copy this new unique number to the next open position
                nonUnique += 1 #The next new integer we see must go right infront of this unique integer
            index += 1 
        return len(nums) - numRemoved #Return the number of unique elements.
            



def main():
    solution = Solution()
    list1 = [0,0,1,1,1,2,2,3,3,4]
    print(solution.removeDuplicates(list1))
    print(str(list1))

if __name__ == "__main__": #Entry point
    main() #Calling main method