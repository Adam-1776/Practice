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
        
        #print(f'median1 = {median1} and median2 = {median2}')
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

def main():
    solution = Solution()
    print(solution.findMedianSortedArrays([1,2],[2,3]))

if __name__ == "__main__": #Entry point
    main() #Calling main method