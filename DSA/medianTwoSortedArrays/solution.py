import math

#https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    #A naive approach, has linear time complexity and verbose code
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
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


#The smart way to do this is to eliminate as much of the solution space as possible. 

def main():
    solution = Solution()
    print(solution.findMedianSortedArrays([1,2],[2,3])) #2.0
    nums1 = [1,1,1,1,10,11,11,11,11]
    nums2 = [8,8,8,8,9,12,12,12,12]
    print(solution.findMedianSortedArrays(nums1,nums2)) #9.5

if __name__ == "__main__": #Entry point
    main() #Calling main method

# [1,1,1,1,10,11,11,11,11] nums1, it's median is 10
# [7,7,8,8,8,8,9,12,12,12,12,13,13] nums2, it's median is 9
# combined median indexs are 10 and 11
# [1,1,1,1,7,7,8,8,8,8,9,10,11,11,11,11,12,12,12,12,13,13] #Combined array, median is 9.5