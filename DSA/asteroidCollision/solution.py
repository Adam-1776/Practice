#https://leetcode.com/problems/asteroid-collision

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if (a + stack[-1]) < 0: #top of stack is destroyed by a
                    stack.pop()
                elif (a + stack[-1]) > 0: #a is destroyed by top of stack
                    break
                else: #both a and top of stack destroy each other
                    stack.pop()
                    break
            else: #This else statement is always executed UNLESS we entered the above while loop AND a break statement was executed
                stack.append(a)
        return stack
         
#No standard algorithm per-se, just careful application of logic is needed for this problem.
#The key thing here is that a collision only takes place if a negative asteroid starts to the right of a positive asteroid
#This is why we only calculate collisions when a negative asteroid is encountered and the top of our stack is positive
#When we encounter this scenario, keep destroying smaller positive asteroids on top of the stack until asteroid a (our negative asteroid)
#has met its match. Then, either:
#   * asteroid a gets destroyed by the top of the stack
#   * or asteroid a gets destroyed alongside the top of the stack if they are both equal
#   * asteroid a gets appended to the stack if there is no positive asteroid greater or equal to it in the stack
#We make handy use of python's while-else loop to solve this problem concisely. Inside our while-loop, we call the break statement if
#asteroid a is not to be appended to our stack.

def main():
    solution = Solution()
    print(solution.asteroidCollision([10,2,-5]))

if __name__ == "__main__": #Entry point
    main() #Calling main method