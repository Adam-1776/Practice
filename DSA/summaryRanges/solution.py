#https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result = []
        left = 0
        right = 0
        while right < len(nums)-1:
            if nums[right] == nums[right+1] - 1:
                right += 1
            elif right != left:
                result.append(str(nums[left]) + "->" + str(nums[right]))
                left = right + 1
                right = left
            else:
                result.append(str(nums[left]))
                left = right + 1
                right = left
        if left == right:
            result.append(str(nums[left]))
        else:
            result.append(str(nums[left]) + "->" + str(nums[right]))
        return result
    

    #Slightly more concise approach
    def summaryRanges2(self, nums: list[int]) -> list[str]:
        result = []
        left = 0
        right = 1
        n = len(nums)
        while left < n:
            currRange = str(nums[left])
            while right < n and nums[right] == nums[right-1] + 1:
                right += 1
            right -= 1 #Decrement right pointer since the while condition is no longer true (i.e. the right pointer has overshot by one at the end of the loop)
            if right != left:
                currRange += "->" + str(nums[right]) #If we found consecutive integers, we can add it to our current range
            left = right + 1 #Everything up to and including right has been accounted for, start from the index after that
            right = left + 1
            result.append(currRange)
        return result
    

    #Even more concise
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res = []
        s = 0 #this is our starting index for each range. The first range starts at index 0 so we initialize it as such
        n = len(nums)
        while s < n:
            e = s #Set end index equal to s
            while e+1 < n and nums[e]+1 == nums[e+1]:
                e+=1 #Keep incrementing e until the nums[e+1] is no longer consecutive to nums[e].
            #e now points to the last index in the current range
            if s == e: #if s and e are equal, only one integer in this range
                res.append(f'{nums[s]}')
            else:
                res.append(f'{nums[s]}->{nums[e]}')
            s = e+1 #Everything till e has been accounted for, move onto the index after that
        return res
    



def main():
    solution = Solution()
    list1 = [0,2,3,4,6,8,9]

    print(solution.summaryRanges(list1))
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method