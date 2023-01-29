#https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        a = 1 #Only one way to climb one step
        b = 2 #Two ways to climb up two steps
        s = 2 #Number of steps we have computed so far
        c = 2 #Number of ways to climb up s steps
        while s < n : #This loop will stop once s == n
            c = a + b #Calculate number of steps for the new s value
            s += 1 #Increment s now that we've computed a value for the new s
            a = b 
            b = c #Fibonacci increment to the last two values
        return c

         
#Using a fibonacci approach. If we define a function f that is the number of ways to climb up x steps, then f(x) = f(x-1) + f(x-2)
#This is because there are only two ways to make the final step to x : climb one step from x-1, or two steps from x-2
#This formula makes this problem ripe for a fibonacci approach. We use variable a to represent number of ways to climb x-2 steps and
#variable b to represent the number of ways to climb x-1 steps.

def main():
    solution = Solution()
    print(solution.climbStairs(44))

if __name__ == "__main__": #Entry point
    main() #Calling main method