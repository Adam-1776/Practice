#https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    #Binary search approach
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        #This condition method checks whether we can get m satisfactory bouquets within a specified number of days
        def dayChecker(day):
            numBouquets = 0
            adjacentFlowers = 0
            for bloom in bloomDay:
                if bloom <= day:
                    adjacentFlowers += 1
                    if adjacentFlowers >= k:
                        numBouquets += 1
                        adjacentFlowers = 0
                else:
                    adjacentFlowers = 0
                if numBouquets >= m : return True
            return False

        #Binary search to minimize the number of days needed to get m bouquets
        left, right = 1, max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if dayChecker(mid):
                right = mid
            else:
                left = mid + 1
        return left if dayChecker(left) else -1
    
    #Slightly more efficient approach
    def minDays2(self, bloomDay: list[int], m: int, k: int) -> int:
        #Simplified the condition method a bit
        def dayChecker(day):
            numBouquets = 0
            adjacentFlowers = 0
            for bloom in bloomDay:
                if bloom > day:
                    adjacentFlowers = 0
                else:
                    adjacentFlowers += 1
                    if adjacentFlowers == k:
                        numBouquets += 1
                        adjacentFlowers = 0
                        if numBouquets >= m : return True
            return False

        if len(bloomDay) < (m*k) : return -1 #If the number of flowers we need exceeds the number of flowers we have, return -1
        left, right = 1, max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if dayChecker(mid):
                right = mid
            else:
                left = mid + 1
        return left

def main():
    solution = Solution()
    print(solution.minDays([1,10,3,10,2],3,1))

if __name__ == "__main__": #Entry point
    main() #Calling main method