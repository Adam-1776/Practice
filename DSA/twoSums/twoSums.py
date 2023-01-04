#https://leetcode.com/problems/two-sum

def twoSum(nums: list[int], target: int) -> list[int]:
    dict = {}
    for n in range(len(nums)):
        temp = target - nums[n]
        if temp in dict:
            return [n,dict[temp]]
        if nums[n] not in dict: #Note: this if condition can be removed, since we know there cannot be two indices with the same value
            dict[nums[n]] = n

#Note that it's important to first check if the value we're looking for is already in the dictionary, before we add the current
#value to the dictionary. This is because if the target sum is 6, and the first number in the list is 3 (for example), the code
#wouldn't work if we added the current value to the dictionary first. We would have added 3 first, and then would have satisfied
#the if-condition since 6-3=3 was just added to the dictionary in the same for loop iteration! Therefore, important to first
#check the dictionary and THEN add the current value to the dictionary in the for loop.

def main():
    print("Read the following integers:")
    with open("input.txt") as f:
        lst = [int(x) for x in f.read().split()]
    #Using 'with' ensures the program doesn't get stuck if there is an I/O error, it's like an alternative to try/catch
    #f.read() returns a string, and split() returns a list of words
    #The way we've defined the list with a for loop is called 'list comprehension'
    print(lst)
    target = 16
    response = twoSum(lst,target)
    print("Values are " + str(lst[response[0]]) + " at index " + str(response[0]) + " and " + str(lst[response[1]]) + " at index " + str(response[1]))

if __name__ == "__main__": #Entry point
    main() #Calling main method