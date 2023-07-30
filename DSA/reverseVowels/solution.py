#https://leetcode.com/problems/reverse-vowels-of-a-string/


class Solution:
    #Two pointers approach. Start pointers from both ends of the list and move them towards each other
    def reverseVowels(self, s: str) -> str:
        seq = list(s) #Convert string to list
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']) #Set of vowels
        l, r = 0, len(seq)-1 #Initialize our pointers to start and end of the list
        while l < r: #Main loop, keep going till the pointers cross each other
            while l < r and seq[l] not in vowels: #Notice how we need to check the main condition l < r inside the sub loops as well! Since we are incrementing the pointer here
                l += 1 #Keep going as long as l is NOT pointing to a vowel
            #After the above loop, l will be pointing to a vowel
            while l < r and seq[r] not in vowels:
                r -= 1
            #Similar loop for r pointer. r will point to a vowel after the above loop
            #Notice that after the above two loops, l or r will point to the next vowels that need to be swapped, OR they will both point to the same index.
            seq[l], seq[r] = seq[r], seq[l] #Since l and r point to the latest vowels that have not been swapped from the left and right sides respectively, we now swap em.
            l += 1
            r -= 1 #Move the pointers
        return "".join(seq)



def main():
    solution = Solution()
    list1 = []

    print(solution.reverseVowels("hello")) #holle
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method