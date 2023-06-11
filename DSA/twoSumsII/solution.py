#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l,r = 0, len(numbers) - 1 #Two pointers approach, start from both ends of the list and move them towards each other
        #Note that this approach only works because numbers list is sorted
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target: #We want the sum of our pointers to become smaller, so move r to the left
                r -= 1
            elif sum < target: #We want the sum of our pointers to become larger, so move l to the right
                l += 1
            else:
                return [l+1 ,r+1] #We add one to the indexes since the problem wants one-indexing
        return None #This line will only be reached if no valid answer exists

def main():
    list1 = [2,7,11,15]
    solution = Solution()
    print(solution.twoSum(list1, 9)) #[1,2]


if __name__ == "__main__": #Entry point
    main() #Calling main method