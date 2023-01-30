from collections import defaultdict

#https://leetcode.com/problems/most-frequent-even-element/

class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        smallest = -1 #Set this to -1 since we return -1 if there are no even elements
        count = 0 #How many times we've seen the most frequent even element
        counter = defaultdict(int) #dictionary with default value of zero
        for n in nums :
            if n % 2 != 0 : continue #Skip this iteration if we have an odd number
            counter[n] += 1 #Increment the count of how many times we've seen this integer
            if counter[n] > count : #If this even number has been seen the most times ...
                smallest = n
                count = counter[n]
            elif counter[n] == count and n < smallest: #If find an even smaller integer that has the same frequency ...
                smallest = n
                
        return smallest

def main():
    solution = Solution()
    list1 = [29,47,21,41,13,37,25,7]
    print(solution.rotate(list1)) # -1

if __name__ == "__main__": #Entry point
    main() #Calling main method