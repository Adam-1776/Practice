#https://leetcode.com/problems/top-k-frequent-elements/


from collections import Counter
import heapq


class Solution:
    #This has linear complexity since Counter() and heapify() have linear complexity, while popping from the heap has O(log(n)) complexity
    #Note that the overall complexity will be O(nlog(n)) if we k = length of list
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency = Counter(nums) #Dictionary where the key is the element, and it's value is it's frequency in nums list
        frequencyTuples = [(value * -1, key) for key,value in frequency.items()] #List comprising of tuples (-frequency, element) for each element in the nums list
        #Note: We multiply the value, or the frequency, by -1 to make heap a max heap
        heapq.heapify(frequencyTuples) #Heapify on the basis of the first value in each tuple, which is the frequency. frequencyTuples is not a maxHeap on the basis of frequency
        result = []
        for _ in range(k): #Pop the first k values from the max heap and append the second value from each returned tuple, which is the element
            result.append(heapq.heappop(frequencyTuples)[1]) #Don't need to check if heap is empty since the problem statement guarantees there are at least k unique values
        return result #result is now a list containing the k most frequent elements


    #Fast approach with linear complexity. This takes advantage of the fact that Counter most_common() method has linear complexity since it uses heap
    def topKFrequent2(self, nums: list[int], k: int) -> list[int]:
        frequency = Counter(nums)
        return [key for key,val in frequency.most_common(k)]



def main():
    solution = Solution()
    list1 = [1,1,1,2,2,3]

    print(solution.topKFrequent(list1, 2)) #[1, 2]
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method