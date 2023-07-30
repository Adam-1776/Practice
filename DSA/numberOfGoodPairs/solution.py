#https://leetcode.com/problems/number-of-good-pairs/


from collections import defaultdict
import math

class Solution:
    #Note, we didn't really need to store a list of all the indexes, simply having the number of times a unique integer is present would be sufficient. We can use Counter() for this
    def numIdenticalPairs(self, nums: list[int]) -> int:
        numIndexes = defaultdict(list)
        for i, num in enumerate(nums):
            numIndexes[num].append(i)

        #numIndexes is now a dictionary that has all the unique integers as it's keys
        #The value of each key is a list of indexes that have that integer in the nums list. Note that these lists are already sorted!
        #Now, if there are n indexes that store a given integer, the number of good pairs for that integer is nC2 (combination formula with
        #size 2 and sample size n). Remember that this formula is n! / (r! * (n-r)!). We can also use the math module.
        #We use combinations instead of permutations since we only want pairs where the first value is smaller than the second. Since order does not matter
        #in combinations, (val1, val2) and (val2, val1) would be considered the same and would only increment goodPairs by one. This effectively elminates the count of 
        #pairs where the first val is higher than the second val.

        goodPairs = 0
        for num in numIndexes:
            if len(numIndexes[num]) >= 2:
                goodPairs += math.comb(len(numIndexes[num]), 2)
        return goodPairs
    

    #Much simpler approach. It still computes the combination implicitly.
    #This approach works because we only want pairs (val1, val2) where val1 is smaller. Therefore when we encounter a new index that stores an integer,
    #We know all the indexes we previously discovered for this integer must be smaller than our current index. Therefore the number of new pairs is equal to the number of
    #indexes we previously had. For example if indexes 1,4,5 have been found for an integer, and we just found a new index 6, we have three new pairs (1,6) (4,6) (5,6)
    def numIdenticalPairs2(self, nums: list[int]) -> int:
        goodPairs = 0
        numIndexes = defaultdict(int) #Dictionary whose keys are unique integers, and value is the number of times that integer has been found in the list so far
        for num in nums:
            goodPairs += numIndexes[num] #We found another integer num in the list. If there are n instances of num in the list, we now have n more good pairs for integer num.
            numIndexes[num] += 1 #Increment the number of indexes that have num
        return goodPairs



def main():
    solution = Solution()
    list1 = [1,2,3,1,1,3]

    print(solution.numIdenticalPairs(list1)) #4
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method