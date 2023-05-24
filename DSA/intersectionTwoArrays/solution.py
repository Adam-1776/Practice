from collections import defaultdict

#https://leetcode.com/problems/intersection-of-two-arrays/
#https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1.intersection(set2))

    #Similar problem as above, only this time the returned list should have each common element present the number of times they are present in both lists
    def intersectII(self, nums1: list[int], nums2: list[int]) -> list[int]:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        for n in nums1:
            dict1[n] += 1
        for n in nums2:
            dict2[n] += 1
        nums3 = []
        dict2keys = dict2.keys()
        for n in dict1:
            if n in dict2keys: #If a number is present in both lists...
                for i in range(min(dict1[n], dict2[n])): #The number of times this num should be present in the return list, is the number of times it was present in both lists
                    nums3.append(n) #Append the number repeatedly to our return list
        return nums3

    #More space efficient approach to intersect II.
    def intersectII_2(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2) : #Expect nums1 to be smaller than nums2 (optional)
            return self.intersect(nums2, nums1) #This if block can be removed
        
        dict1 = defaultdict(int)
        nums3 = []
        for n in nums1:
            dict1[n] += 1
        #This time, we only store values of nums1 in memory.
        #Our technique here is to recognize that the number of times an integer appears in nums1
        #is the greatest number of times it could appear in our intersection. This is also true for nums2 of course
        for num in nums2:
            if num in dict1: #If a num is present in both nums1 and nums2...
                dict1[num] -= 1 #Decrement the count of this num in the dictionary, since we adding this number to our intersection list
                if dict1[num] == 0 : dict1.pop(num) #Remove this num from the dictionary if its count is now zero because the frequency in nums1 is exhausted
                nums3.append(num) #Add this num to our list
        return nums3

    #Approach to use if the lists are sorted
    def intersectII_3(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()
        #The sorting can be skipped if the lists are already sorted
        ans = []
        i = j = 0 #Two pointers approach. i is the pointer for nums1 and j is the pointer for nums2
        while i < len(nums1) and j < len(nums2): #Keep going until either of the lists has been traversed
            if nums1[i] < nums2[j]: #We want to get both pointers to have the same value
                i += 1
            elif nums1[i] > nums2[j]: #So we nudge either pointer so that they'll both point to the same value
                j += 1
            else: #If both pointers are pointing to indexes with the same value, then we nudge them both forward
                ans.append(nums1[i]) #Append this value to our list
                i += 1
                j += 1
        return ans


def main():
    solution = Solution()
    nums1 = [1,1,2,3,3,3,3,7,6,6,4,7]
    nums2 = [1,4,3,3,8,7]
    print(solution.intersection(nums1,nums2)) #[1, 3, 4, 7]
    print(solution.intersectII(nums1,nums2)) #[1, 3, 3, 7, 4]

if __name__ == "__main__": #Entry point
    main() #Calling main method