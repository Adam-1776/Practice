#https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = [] #This stack holds the indexes for which we NOT yet found the answer (i.e. when next a higher temperatures occurs)
        #This stack naturally ends up as a monotonic stack since the values in it are in non-increasing order. This is because the the moment we find a larger temperature
        #than the index at the top of the stack, we have found the answer to the top of the stack and possibly other indexes in the stack below too.
        results = [0] * len(temperatures)
        for i in range(len(temperatures)):
            #print(f'stack = {stack}')
            if stack and temperatures[i] <= temperatures[stack[-1]]: #Current temperatures is less than or equal to top of stack
                stack.append(i)
                #print('Added index {i} to stack since it is smaller than top of stack')
            else: #The current value is bigger than the top of stack, or the stack is empty...
                while stack and temperatures[stack[-1]] < temperatures[i]: #While the current value is greater than top of stack...
                    poppedIndex = stack.pop() #We have found index i to be the next day where the temperature exceeds index at top of the stack
                    results[poppedIndex] = (i - poppedIndex) #The number of days after which higher temperature occurs after index poppedIndex
                    #print(f'Popped stack since we found higher temperature at {i}')
                stack.append(i)
                #print(f'Added index {i} to stack')
        return results
    
    #More concise solution
    def dailyTemperatures2(self, temperatures: list[int]) -> list[int]:
        stack = []
        results = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]: #While we the current index is hotter than the top of stack...
                poppedIndex = stack.pop() #We have found the answer to the top of the stack
                results[poppedIndex] = (i - poppedIndex) #Compute the answer for index at top of stack and record this result
            stack.append(i) #We always need to append i to the stack, since we have not yet found the answer for index i
        return results



def main():
    solution = Solution()
    print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method