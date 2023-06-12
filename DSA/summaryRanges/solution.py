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
            right -= 1
            if right != left:
                currRange += "->" + str(nums[right])
            left = right + 1
            right = left + 1
            result.append(currRange)
        return result



def main():
    solution = Solution()
    list1 = [0,2,3,4,6,8,9]

    print(solution.summaryRanges(list1))
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method