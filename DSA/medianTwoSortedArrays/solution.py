import math

#https://leetcode.com/problems/median-of-two-sorted-arrays/
#Solution: https://youtu.be/NTop3VTjmxk
class Solution:

    def isPartitionValid(self, left1v, left2v, right1v, right2v) -> int:
        if left1v <= right2v:
            if left2v <= right1v:
                print("Correct partition found")
                return 0
            else:
                print("Need to move left1 upwards")
                return 1
        else:
            print("Need to move left1 downwards")
            return -1

    #A somewhat better but convoluted technique that uses partitioning
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        if len(nums1) == 0 and len(nums2) == 0 :
            return 0.0

        if len(nums1) == 0:
            if (len(nums2)) % 2 != 0:
                return nums2[(len(nums2)) // 2]
            else:
                return (nums2[(len(nums2) - 1) // 2] + nums2[(len(nums2)) // 2]) / 2

        if len(nums2) == 0:
            if (len(nums1)) % 2 != 0:
                return nums1[(len(nums1)) // 2]
            else:
                return (nums1[(len(nums1) - 1) // 2] + nums1[(len(nums1)) // 2]) / 2

        k = (len(nums1) + len(nums2) + 1) // 2
        right1 = (len(nums1) + 1) // 2
        while True:
            left1 = right1 - 1
            right2 = k - right1
            left2 = right2 - 1 
            print(f'left1 and left2 are {left1} and {left2}')
            print(f'right1 and right2 are {right1} and {right2}')
            left1v = -9999999999 if (left1 < 0 or left1 >= len(nums1)) else nums1[left1]
            left2v = -9999999999 if (left2 < 0 or left2 >= len(nums2)) else nums2[left2]
            right1v = nums1[right1] if right1 < len(nums1) else 9999999999
            right2v = nums2[right2] if right2 < len(nums2) else 9999999999
            print(f'left1v and right1v are {left1v} and {right1v}')
            print(f'left2v and right2v are {left2v} and {right2v}')
            if self.isPartitionValid(left1v, left2v, right1v, right2v) == 0 :
                if (len(nums1) + len(nums2)) % 2 != 0:
                    return max(left1v,left2v)
                else:
                    return (max(left1v,left2v) + min(right1v,right2v)) / 2
            elif self.isPartitionValid(left1v, left2v, right1v, right2v) == -1:
                shift = right1 // 2
                right1 -= 1
            else:
                shift = (right1 + len(nums1) - 1) // 2
                right1 += 1

    #A naive approach, has linear time complexity and verbose code
    def findMedianSortedArrays2(self, nums1: list[int], nums2: list[int]) -> float:
        list1 = []
        odd = True
        median1 = 0
        median2 = 0
        if (len(nums1) + len(nums2)) % 2 == 0:
            odd = False
            median2 = int((len(nums1) + len(nums2)) / 2)
            median1 = median2 - 1
        else:
            median1 = math.floor((len(nums1) + len(nums2)) / 2)
        
        print(f'median1 = {median1} and median2 = {median2}')
        index1 = 0
        index2 = 0
        count = 0
        while index1 < len(nums1) or index2 < len(nums2):
            if index1 == len(nums1) :
                list1 += nums2[index2:]
                break
            if index2 == len(nums2) :
                list1 += nums1[index1:]
                break
            if nums1[index1] < nums2[index2]:
                list1.append(nums1[index1])
                index1 += 1
                count += 1
            elif nums1[index1] > nums2[index2]:
                list1.append(nums2[index2])
                index2 += 1
                count += 1
            else:
                list1.append(nums1[index1])
                list1.append(nums2[index2])
                index1 += 1
                index2 += 1
                count += 2
            if count > median1+1 :
                if odd == True:
                    return float(list1[median1])
                else:
                    return float((list1[median1] + list1[median2]) / 2)
    
        if odd == True:
            return float(list1[median1])
        else:
            return float((list1[median1] + list1[median2]) / 2)

    def findMedianSortedArrays3(self, nums1: list[int], nums2: list[int]) -> float:
        size = (len(nums1) + len(nums2)) // 2 #Length we expect for half the hypothetical combined array
        l1 = len(nums1) // 2 #For starters, pick half of nums1
        l2 = size - l1 #For starters, get the remaining values from the left from nums2
        #We have now picked enough elements from nums1 and nums2 to equal the first half of the combined array. len(nums1[:l1]) + len(nums2[:l2]) == size 
        #Above, we've picked left pointer for each of the two lists, combined these are the left half of the hypothetical final combined array.
        #In other words, the first half of the hypothetical combined array would include all values from nums1[:l1] and nums2[:l2] in unknown order.
        #We chose the above portions of nums1 and nums2 arbitrarily and they probably don't correctly form the first half of the combined array, but we fix this
        while True:
            print(f'l1 and l2 are {l1} and {l2}')
            if nums1[l1-1] < nums2[l2] : #If the last element of the nums1 partition we chose is smaller than the first element of the right partition of nums2 ...
                if nums2[l2-1] < nums1[l1]: #If the first element of the nums2 partition we chose is smaller than the first element of the right partition of nums1 ...
                    val1 = max(nums1[l1-1], nums2[l2-1]) #Then our partition is correct
                    val2 = min(nums1[l1], nums2[l2]) # Median can be found from the biggest element in the left partitions and the smallest element in the right partitions
                    print(f'Median values are {val1} and {val2}')
                    return
                else: #If the 
                    print(f'We need to move l1 rightwards and l2 leftwards')
                    l1 += 1; l2 -=1;
            else:
                print(f'We need to move l1 leftwards and l2 rightwards')
                l1 -= 1; l2 +=1;
            return 0

        



#The smart way to do this is to eliminate as much of the solution space as possible, which you can do using binary search.


def main():
    solution = Solution()
    #print(solution.findMedianSortedArrays([1,2],[2,3])) #2.0
    nums1 = [1,1,1,1,10,11,11,11,11]
    nums2 = [8,8,8,8,9,12,12,12,12]
    nums3 = nums1 + nums2; nums3.sort()
    print(nums3)
    #print(solution.findMedianSortedArrays2(nums1,nums2)) #9.5
    print(solution.findMedianSortedArrays(nums1,nums2))

if __name__ == "__main__": #Entry point
    main() #Calling main method

# [1,1,1,1,10,11,11,11,11] nums1, it's median is 10
# [7,7,8,8,8,8,9,12,12,12,12,13,13] nums2, it's median is 9
# combined median indexs are 10 and 11
# [1,1,1,1,7,7,8,8,8,8,9,10,11,11,11,11,12,12,12,12,13,13] #Combined array, median is 9.5