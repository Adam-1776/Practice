#https://leetcode.com/problems/integer-to-roman/

class Solution:
    #Verbose but logically simple solution. We minimize complexity by considering subtraction cases such as IX and CM as it's own digit
    #Check the greatest digit that can be added in each iteration. It has linear complexity with respect to the number of digits
    #since the time to find each digit is constant
    def intToRoman(self, num: int) -> str:
        roman = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        result = ""
        romanVals = sorted(list(roman), reverse = True) #List of keys of roman in reverse order since we want to check them from greatest to least
        while num != 0: #Keep going till num is zero
            for romanVal in romanVals: #Iterate over romanVals in greatest to least order
                if romanVal <= num: #Found the next roman digit to be added
                    result += roman[romanVal]
                    num -= romanVal #Subtract num by the the value of the roman digit that was added
                    break

        return result
    

    #Clever and fast solution, might be too verbose for interviews
    def intToRoman2(self, num):
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hrns = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        ths = ["", "M", "MM", "MMM"]
        #Use the % operator to shave off digits from the right side before dividing
        return ths[num / 1000] + hrns[(num % 1000) / 100] + tens[(num % 100) / 10] + ones[num % 10]



def main():
    solution = Solution()
    print(solution.intToRoman(1994)) #MCMXCIV
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method