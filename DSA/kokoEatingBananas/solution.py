import math
#https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def numHours(k) :
            if k == 0 : return 99999999999
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
                if hours > h : return 99999999999 #If we have exceeded the time limit, end the loop now
            return hours

        left = math.floor(sum(piles) / h)
        right = max(piles)
        #Binary search. Setting it up this way will give us the smallest k that fits the criteria
        while left < right :
            mid = (left + right) // 2
            hours = numHours(mid)
            #print(f'left = {left} and right = {right} and mid = {mid}')
            if hours <= h : #There may be multiple k values will lead to hours less or equal to h, but we want the smallest one
                right = mid
            elif hours > h :
                left = mid + 1
        return right

    


def main():
    solution = Solution()
    print(solution.minEatingSpeed([30,11,23,4,20])) #23

if __name__ == "__main__": #Entry point
    main() #Calling main method