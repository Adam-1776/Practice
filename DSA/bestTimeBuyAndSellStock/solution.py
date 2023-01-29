#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        bestProfit = 0
        lowestPrice = 9999999
        for p in prices:
            if p < lowestPrice : lowestPrice = p
            elif p - lowestPrice > bestProfit :
                bestProfit = p - lowestPrice
        return bestProfit

         
#Two pointer approach, but we don't track the indexes directly since the problem only asks us to return the best profit, not the actual days
#in which we should buy and sell. Track the lowest price seen so far, and the best profit seen so far.

def main():
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4])) #5

if __name__ == "__main__": #Entry point
    main() #Calling main method