#https://leetcode.com/problems/target-sum/

from collections import defaultdict

class Solution:
    #Recursive DFS with memoization. A bit confusing due to the way data and indices are kept.
    #When we call the recursive DFS, the dictionary is filled starting with the last indexes. UNSURE whether this is top down or bottoms up
    def findTargetSumWays(self, nums: list[int], target: int) -> int:     
        dic = defaultdict(int) #Key is tuple(index, total) and value is the number of ways to reach (len(nums), target)
        #In the tuple above, index is the number of values in the list we have computed so far, and total is the sum of those computed values
        #For instance dic[(3,4)] = 5 means that there are five ways to reach our target (len(nums), target) if we have processed the first three values and the total sum is 4
        #We want to find the value of dic[(0,0)] which is the number of ways to reach the target when haven't processed any elements in the list yet.
        
        #dfs() computes the number of ways to reach target when we're initially at (index, total sum so far)
        def dfs(index=0, total=0): #Initially, we have processed zero indexes and have a total sum of zero     
            key = (index, total)
            
            if key not in dic: #We do not yet know how many ways there are to reach value 'total' after processing 'index' values in nums
                if index == len(nums): #If we have processed all the numbers in nums list...                   
                    return 1 if total == target else 0 #Terminal case for recursion is when we've processed the entire list
                else:
                    #Number of ways to reach target from (index, total) is take combined values of add and subtract the current total from the value at the current index.
                    #The line below may look confusing but think about it. 'index' is one greater than the actual index that we've actually computed till now. And 'total' is
                    #the value till 'index'. So to move onto the next index, add and subtract the current 'index' to the total. Basically 'total' is the sum BEFORE index 'index'
                    #in the nums list.
                    dic[key] = dfs(index+1, total + nums[index]) + dfs(index+1, total - nums[index])                    
                        
            return dic[key] #Additional terminal case is where we already have the value of (index, total). This is where memoization kicks in.                                                             
                
        return dfs()

         
#Need to study this further!!
def main():
    solution = Solution()
    print(solution.findTargetSumWays([1,1,1,1,1], 3)) #5

if __name__ == "__main__": #Entry point
    main() #Calling main method