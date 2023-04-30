#https://leetcode.com/problems/find-k-th-smallest-pair-distance/
#https://youtu.be/ym93rTBR4j8

class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        #Are there at least k pairs exist whose distance does not exceed the specified distance?
        #i.e. Is this at least the kth smallest distance?
        #This condition helper method uses a two pointers approach
        def checkDistance(distance):
            numPairs = 0
            left, right = 0, 1
            lenNums = len(nums)
            while left < lenNums or right < lenNums: #Keep going until both pointers are the end
                #In the while loop below, keep incrementing right till it either reaches the end of the list or we breach the distance limit
                while (right < lenNums) and (abs(nums[right] - nums[left]) <= distance):
                    right += 1
                #variable right now points to the index that no longer has a distance within limits with left
                #OR, right may equal lenNums

                #Pairs within indices [left, right-1] are guaranteed to be within the specified distance
                numPairs += right - left - 1 #Add the number of pairs that start with left until right-1
                #eg pairs (left, right-3), (left, right-2), (left, right-1) are three such pairs
                if numPairs >= k : return True
                left += 1
            return False


        #Use binary search to find the smallest distance such that there are at least k pairs whose distances are within that distance
        nums.sort()
        left, right = 0, (nums[-1] - nums[0])
        while left < right:
            mid = left + (right - left) // 2
            if checkDistance(mid):
                right = mid
            else:
                left = mid + 1
        return left

def main():
    solution = Solution()
    print(solution.smallestDistancePair([1,3,1],1))

if __name__ == "__main__": #Entry point
    main() #Calling main method