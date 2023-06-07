#https://leetcode.com/problems/container-with-most-water/

class Solution:
    #Brilliant two pointers solution. Optionally records the indexes where the most water capacity was found
    #NOTE: More study needed on how this works
    def maxArea(self, height: list[int]) -> int:
        bestLines = [0,0]
        mostWater = 0

        def amountWater(l, r):
            return (r - l) * min(height[l], height[r])

        l, r = 0, len(height) - 1
        while l < r:
            lHeight = height[l]
            rHeight = height[r]
            if lHeight > rHeight:
                capacity = amountWater(l,r)
                if capacity > mostWater:
                    mostWater = capacity
                    bestLines = [l,r]
                r -= 1
            else:
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