#https://leetcode.com/problems/shortest-word-distance/


class Solution:
    #Linear complexity
    def shortestDistance(self, words, word1, word2):
        word1Indexes = list()
        word2Indexes = list()
        for i in range(len(words)):
            if words[i] == word1:
                word1Indexes.append(i)
            elif words[i] == word2:
                word2Indexes.append(i)
        #word1Indexes and word2Indexes now contain the indexes where word1 and word2 are present in the list. Note that they are already sorted!
        leastDistance = 9999
        index1, index2 = 0, 0 #Two pointers to keep track of the index we are processing in words1Indexes and words2Indexes respectively
        #In the below loop, we will update index1 and index2 such that words1Indexes[index1] will be the closest value to words2Indexes[index2]
        #We are using an approach similar to merging two sorted arrays (such as how it's done in merge sort)
        while index1 < len(word1Indexes) and index2 < len(word2Indexes): #If word1Indexes has the smaller index...
            if word1Indexes[index1] < word2Indexes[index2]:
                leastDistance = min(leastDistance, (word2Indexes[index2] - word1Indexes[index1]))
                index1 += 1 #Increment index1 since we are done comparing index1 with its closest index2
            else: #If words2Indexes has the smaller index...
                leastDistance = min(leastDistance, (word1Indexes[index1] - word2Indexes[index2]))
                index2 += 1
        return leastDistance

    
    #This does NOT work!! This attempt failed because it failed to consider all combinations of indexes with word1 and word2
    #This is because it only considers the rightmost word2 and leftmost word1 at a time, so it failed to consider b and a which are the last two entries in the list.
    def shortestDistance2(self, words, word1, word2):
        leastDistance = 9999
        n = len(words)
        index1, index2 = 0, n - 1
        while index1 < n and index2 >= 0:
            while index1 < n-1 and  words[index1] != word1:
                index1 += 1
            while index2 > 0 and words[index2] != word2:
                index2 -= 1
            if words[index1] == word1 and words[index2] == word2:
                leastDistance = min(leastDistance, abs(index2 - index1))
            index1 += 1
            index2 -= 1
        return leastDistance
    



def main():
    #words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    #word1 = "fox"
    #word2 = "dog"
    words = ["a", "c", "d", "b", "a"]
    word1 = "a"
    word2 = "b"
    solution = Solution()

    print(solution.shortestDistance(words, word1, word2)) #5
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method