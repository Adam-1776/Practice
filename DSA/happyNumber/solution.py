#https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:

        def convert(num) : #Inner helper function
            digits = list(str(num))
            digits = map(lambda x : int(x) ** 2 , digits)
            return sum(digits)

        def convert2(num) : #Alternate Inner helper function using list comprehension
            digits = [int(i)**2 for i in str(num)]
            return sum(digits)
        
        seen = set()
        while(True) :
            conversion = convert(n)
            print(f'n = {n} and conversion = {conversion}')
            if conversion == 1 : #If the conversion leads to 1, it's a happy number
                return True
            if conversion in seen : #If the conversion is a number we've EVER seen before, it is not a happy number
                return False
            n = conversion #Haven't found a repeating sequence yet, gotta keep going
            seen.add(conversion)


def main():
    solution = Solution()
    print(solution.isHappy(19)) #True

if __name__ == "__main__": #Entry point
    main() #Calling main method