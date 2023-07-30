#https://leetcode.com/problems/shortest-word-distance/


class Solution:

    #Simplest approach with two pointers, both pointers start from the left. Linear complexity
    def shortestDistance(self, words, word1, word2):
        shortestDistance = len(words) # Initialize the shortest distance with the length of the words list
        position1, position2 = -1, -1 # Initialize the positions of word1 and word2 with -1
        for i, word in enumerate(words):
            if word == word1: # If the current word is word1, update position1
                position1 = i
            elif word == word2: # If the current word is word2, update position2
                position2 = i
            #If both the positions are valid, check their distance. Note that position1 and position2 pointers will not be updated in every iteration of this loop
            if position1 != -1 and position2 != -1:
                shortestDistance = min(shortestDistance, abs(position1 - position2))
        return shortestDistance


    #Two pointers approach, both start from the left. Linear complexity
    def shortestDistance2(self, words, word1, word2):
        n = len(words)
        shortestDistance = 9999
        l = min(words.index(word1), words.index(word2)) #Start with the smallest index that has either word
        r = l + 1
        #In this loop, the l pointer always points to the rightmost occurance of either word1 or word2 that has been discovered
        while l < n and r < n:
            while r < n and words[r] != word1 and words[r] != word2:
                r += 1
            #r now points to the next index after l that has either word1 or word2, OR it's past the end of the list
            if r < n and words[r] == words[l]: #Both l and r point to the same word
                l = r #Since we found a new rightmost index with this word, update l and r pointers
                r = l + 1
            else: #l and r now point to two different words! Check their distance
                shortestDistance = min(shortestDistance, (r - l))
                l = r #Now we have a new l value that we will continue our search from
                r = l + 1
        return shortestDistance



    #Linear complexity
    def shortestDistance3(self, words, word1, word2):
        word1Indexes = list()
        word2Indexes = list()
        for i in range(len(words)):
            if words[i] == word1:
                word1Indexes.append(i)
            elif words[i] == word2:
                word2Indexes.append(i)
        #word1Indexes and word2Indexes now contain the indexes where word1 and word2 are present in the list. Note that they are already sorted!
        #We have to store the indexes of word1 and word2 in two seperate lists instead of one list in case two copies of the same word are next to each other in the list.
        #We are looking for the smallest value between two DIFFERENT words so we need to differentiate the indexes of those two words.
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
    #Attempted to use a two pointers approach starting from both ends and moving inwards but this doesn't work for this problem.
    def shortestDistance4(self, words, word1, word2):
        leastDistance = 9999
        n = len(words)
        index1, index2 = 0, n - 1
        while index1 < n and index2 >= 0:
            while index1 < n and  words[index1] != word1:
                index1 += 1
            #index1 now equals word1 OR it's past the end of the list
            while index2 >= 0 and words[index2] != word2:
                index2 -= 1
            #index2 now equals word2 OR it's behind the start of the list
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

    print(solution.shortestDistance(words, word1, word2)) #1
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method