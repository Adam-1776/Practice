#https://leetcode.com/problems/search-insert-position/

class Solution:
    #Binary search solution
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            #print(f'left = {left} and right = {right}')
            mid = (left + right) // 2
            if target < nums[mid]: #Target is to the left of mid
                right = mid - 1
            elif target > nums[mid] : #Target is to the right of mid
                left = mid + 1
            else:
                return mid
        return left #The loop exits when left is greater than right. Left points to the index where the target should have been
            

def main():
    solution = Solution()
    list1 = [20,21,24,25]
    print(solution.searchInsert(list1,23))

if __name__ == "__main__": #Entry point
    main() #Calling main method