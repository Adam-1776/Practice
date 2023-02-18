from collections import defaultdict

#https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        indexMap = defaultdict(list)
        for i in range(len(nums)):
            if nums[i] in indexMap:
                for j in indexMap[nums[i]]:
                    if abs(i - j) <= k : return True
            indexMap[nums[i]].append(i)
        return False



def main():
    solution = Solution()
    print(solution.containsNearbyDuplicate([1,2,3,1,2,3], 2)) #False

if __name__ == "__main__": #Entry point
    main() #Calling main method