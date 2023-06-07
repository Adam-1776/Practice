#https://leetcode.com/problems/3sum/


from collections import defaultdict

class Solution:
    #Fast and extremely clever solution, need to study this further to understand how it works
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        negative = defaultdict(int)
        positive = defaultdict(int)
        zeros = 0
        for num in nums:
            if num < 0:
                negative[num] += 1
            elif num > 0:
                positive[num] += 1
            else:
                zeros += 1
        
        result = []
        if zeros:
            for n in negative:
                if -n in positive:
                    result.append((0, n, -n))       
            if zeros > 2:
                result.append((0,0,0))

        for set1, set2 in ((negative, positive), (positive, negative)): #This for-loop runs twice.
            #In the first iteration of this for loop, set1 is negative defaultdict and set2 is positive defaultdict
            #In the second iteration of this for loop, set1 is positive defaultdict and set2 is negative defaultdict
            #print(f'set1 = {set1}')
            #print(f'set2 = {set2}\n\n')
            set1Items = list(set1.items()) #List of key-value pairs in set1. Each element in this list is a tuple (num, frequency)
            #print(f'set1Items = {set1Items}')
            for i, (j, k) in enumerate(set1Items): # i is the index of list set1Items and (j,k) is a tuple (num, frequency) of set1
                #Only considering pair (j,k) at set1Items[i] while entering below for-loop
                for j2, k2 in set1Items[i:]: #
                    if j != j2 or (j == j2 and k > 1): #If the two nums j and j2 are different we can proceed. Or we can proceed if they are equal but that num is present multiple times
                        if -j-j2 in set2: #We have two numbers j and j2 that could form a 3sum. If (-j-j2) is also present, then we have found a 3sum
                            result.append([j, j2, -j-j2])
        return result



def main():
    solution = Solution()
    list1 = [-1,0,1,2,-1,-4]

    print(solution.threeSum(list1)) #[[-1,-1,2],[-1,0,1]]
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method