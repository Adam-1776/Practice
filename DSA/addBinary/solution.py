#https://leetcode.com/problems/add-binary/

class Solution:
    #Solution using Python binary functions
    def addBinary(self, a: str, b: str) -> str:
        numA = int(a,2)
        numB = int(b,2)
        return bin(numA+numB)[2:]

    #Solution with manual implementation
    def addBinary2(self, a: str, b: str) -> str:
        indexA = len(a) - 1
        indexB = len(b) - 1
        carry = 0
        ans = []
        while indexA >= 0 or indexB >= 0 or carry > 0: #Same logic as adding two numbers in a list
            numA = int(a[indexA]) if indexA >= 0 else 0
            numB = int(b[indexB]) if indexB >= 0 else 0
            val = (numA + numB + carry) % 2
            carry = (numA + numB + carry) // 2
            ans.append(str(val)) #Conver the val to a string before appending it to the list to make it easy to join the list to a string
            indexA -= 1
            indexB -= 1
        return ''.join(ans[::-1]) #Join all the strings in the list to a single string, while reversing the list


def main():
    solution = Solution()
    print(solution.addBinary("1010" , "1011")) #10101
    print(solution.addBinary2("1010" , "1011")) #10101


if __name__ == "__main__": #Entry point
    main() #Calling main method