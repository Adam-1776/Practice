from collections import defaultdict
#https://leetcode.com/problems/find-the-town-judge/


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        # [a,j] will exist for every value a except j
        # [j,a] will never exist for any value a
        trustedBy = defaultdict(int) #Dictionary where the key is the person, and the value is the number of people they are trusted by
        #We setup a defaultdict with default value 0 for convenience. 
        candidates = set(i for i in range(1,n+1)) #Set of people who trust no one. Initializing with all people 1 through n
        for i in trust:
            candidates.discard(i[0]) #Person i[0] trusts someone, so remove them from set of possible candidates
            trustedBy[i[1]] += 1 #Person i[1] is trusted by someone, so increment their trusted count. We can do this since the problem statement guarantees all pairs are unique

        #Now that we've analyzed all the trust relationships, analyze to find the judge
        for c in candidates: #Anyone who trusts someone has already been eliminated from candidates. All candidiates left in the set trust no one
            if trustedBy[c] == n-1 : return c #If a candidate is trusted by everyone but himself, he must be the town judge
        
        return -1 #This line is only reached if no judge is present.

    #findJudge2 is identical to findJudge except we use a list instead of a defaultdict
    def findJudge2(self, n: int, trust: list[list[int]]) -> int:
        trustedBy = [0] * (n+1)
        candidates = set(i for i in range(1,n+1))
        for i in trust:
            trustedBy[i[1]] += 1
            candidates.discard(i[0])

        for c in candidates:
            if trustedBy[c] == n-1 : return c
        
        return -1
         


def main():
    solution = Solution()
    print(solution.findJudge(3, [[1,3],[2,3],[3,1]])) #-1
    print(solution.findJudge(3, [[1,3],[2,3]])) #3


if __name__ == "__main__": #Entry point
    main() #Calling main method