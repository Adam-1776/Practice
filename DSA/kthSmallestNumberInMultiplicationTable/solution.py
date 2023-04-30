#https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

class Solution:
    #Binary search solution
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        #Condition: are there at least k values inside the multiplication table that <= num ?
        def checkPosition(num):
            smallerValues = 0 #Number of values in the table found that are <= num
            for row in range(1, m+1): #Traverse the table row by row
                smallerValues += min((num // row), n) #How many integers in this row that are <= num? Add it to our count
                if smallerValues >= k : return True
            return False

        #Use binary search to find the minimum value in the table that satisfies checkPosition()
        #Notice that we do not have to worry about ending up with a value that is not in the table, since the *minimum*
        #value that meets checkPosition() will necessarily be in our multiplication table and will be exactly the kth smallest
        #value in the multiplication table. This is because the kth smallest value is the smallest value that will have
        #k values in the table smaller than or equal to kth smallest value. 
        left, right = 1, (m*n) #We know the values in the table range from [1, m*n], this is out search space
        while left < right:
            mid = left + (right - left) // 2
            if checkPosition(mid):
                right = mid
            else:
                left = mid + 1
        return left

def main():
    solution = Solution()
    print(solution.findKthNumber(2,3,6))

if __name__ == "__main__": #Entry point
    main() #Calling main method