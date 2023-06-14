# https://leetcode.com/problems/first-bad-version/


def isBadVersion(n: int):
    #Dummy method
    return True

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        #Use binary search to find the smallest index where isBadVersion() condition returns True
        while l < r:
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l



def main():
    print("No test case")
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method