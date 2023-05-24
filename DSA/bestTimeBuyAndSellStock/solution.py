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
    
    #Sliding window approach that keeps track of the indexes
    def maxProfit2(self, prices: list[int]) -> int:
        bestProfit = 0
        bestDays = [0,0] #Store the indexes representing best days to buy and sell
        l, r = 0,1
        #Condition: keep moving r until find the lowest price yet, then set l to that index with the lowest price
        #In each iteration check if we've maximized the profit found so far
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            if prices[r] - prices[l] > bestProfit:
                bestProfit = prices[r] - prices[l]
                bestDays[0], bestDays[1] = l, r
            r += 1
        return bestProfit

         
#Two pointer approach, but we don't track the indexes directly since the problem only asks us to return the best profit, not the actual days
#in which we should buy and sell. Track the lowest price seen so far, and the best profit seen so far.

def main():
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4])) #5

if __name__ == "__main__": #Entry point
    main() #Calling main method