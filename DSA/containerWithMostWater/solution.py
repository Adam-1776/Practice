#https://leetcode.com/problems/container-with-most-water/

class Solution:
    #Brilliant two pointers solution. Optionally records the indexes where the most water capacity was found
    def maxArea(self, height: list[int]) -> int:
        bestLines = [0,0]
        mostWater = 0

        def amountWater(l, r):
            return (r - l) * min(height[l], height[r])

        #Two pointers approach where l and r start at both ends of the list and move towards each other
        l, r = 0, len(height) - 1
        while l < r:
            lHeight = height[l]
            rHeight = height[r]
            if lHeight > rHeight: #If left pointer is taller, hold left and instead move right leftwards
                capacity = amountWater(l,r)
                if capacity > mostWater:
                    mostWater = capacity
                    bestLines = [l,r]
                r -= 1
            else: #Else, hold right pointer and move left pointer forwards
                capacity = amountWater(l,r)
                if capacity > mostWater:
                    mostWater = capacity
                    bestLines = [l,r]
                l += 1
        
        return mostWater



def main():
    solution = Solution()
    list1 = [1,8,6,2,5,4,8,3,7]

    print(solution.maxArea(list1)) #49
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method