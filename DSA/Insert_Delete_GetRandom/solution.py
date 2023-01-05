import collections
import random
#https://leetcode.com/problems/insert-delete-getrandom-o1/
#https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

#Implement set with insertion, deletion, and get random value in O(1)
class RandomizedSet:
    def __init__(self):
        self.List = []
        self.Dict = {}
        #Initialize an empty list and an empty dictionary
        #The list stores the actual values, and the dictionaty is used to store the index in the list where each val is stored
        #This approach with two data structures is highly effective to keep time complexity down. It enables us to have the advantages of a list
        #such as random access, while also being able to locate the index of a particular value instantly in the list using the dictionary.
        #The reason we don't simply use a Python set is because it is extremely inefficient to pick a random item from a Python set.
        #Conversely, picking a random item from a list is a constant-time operation, since lists are designed for random access.


    def insert(self, val: int) -> bool:
        if val in self.Dict:
            return False #Return if the value is already in the set
        self.Dict[val] = len(self.List) #Since we'll append to the end of the list, we know it's index will be the current length of the list
        self.List.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.Dict:
            return False #Return false if the value is absent from the set

        valIndex = self.Dict[val] #Index of value to be removed
        swapVal = self.List[-1] #Value of the item in the list
        self.List[valIndex] = swapVal #Replace the index of the item to be removed with the last value of the list
        self.Dict[swapVal] = valIndex #Update the index of the swapped item
        self.Dict.pop(val) #Remove the deleted item from the dictionary
        self.List.pop() #The last item of the item is now duplicated, since we copied it to the index of the deleted item. Thus removing this last item
        #We've basically swapped the item to be removed and the last item of the list, and then popped the last item of the list.
        #This enables us to delete the selected item from the list in O(1) time. We can do this since order of the list does not matter.
        return True

    def getRandom(self) -> int:
        return random.choice(self.List) #This line returns a random value from the list

#Implement multiset with insertion, deletion, and get random value in O(1)
class RandomizedCollection:

    def __init__(self):
        self.List = []
        self.Dict = {}
        # self.Dict = collections.defaultdict(set) #This is an alternate way to create an empty dictionary. This way it is already setup to take sets as its value
        #Initialize an empty list and an empty dictionary
        #The list stores the actual values, and the dictionaty is used to store the indices in the list where each val is stored

    def insert(self, val: int) -> bool:
        #print("Inserting " + str(val)) #Commenting print statements since it slows down execution time in Leetcode
        if val in self.Dict:
            self.Dict[val].add(len(self.List)) #If val is in the dict, add to its set the size of the list -- since we will add the val to the end of the list
            self.List.append(val) #Append the val to the end of the list. We added this index to the dict in the line above
            #print(self.Dict)
            return False #Return false since the value was already in the multiset
        
        self.Dict[val] = {len(self.List)} #If this is a new val, we initialize the dictionary with a set with just one value -- the length of the list
        #We add the length of the list since we will append this new val at the end of the list. Note the curly brackets in the assignment, this is necessary
        #to tell Python that the value we're storing in the dictionary is of type set.
        
        self.List.append(val) #We always append incoming vals to the end of the list
        #print(self.Dict)
        return True #Return true since this is a new val not already in the multiset
        
    def remove(self, val: int) -> bool:
        #print("Removing " + str(val))
        if val not in self.Dict:
            #print(self.Dict)
            return False #Return false since this val is already absent in the multiset

        valIndex = self.Dict[val].pop() #This line is key! It picks a random value from the set of indices holding val, AND it removes it from the set
        swapVal = self.List[-1] #The value we're going to use to swap is the last item in the list
        self.Dict[swapVal].add(valIndex) #Adding the index to be removed to the set of indices for the swap value, since we're going to replace this index with the swap value
        self.List[valIndex] = swapVal #Replacing the index to be removed with the swap value. Added this new index to the swap value's set in the line above
        self.Dict[swapVal].discard(len(self.List)-1) #The last item in the list is a duplicate of the swap value. We're going to remove it from the set of indices
        self.List.pop() #The last item inthe list is a duplicate of the swap value. Removing it from the list. Already removed it from the dictionary in the line above
        #print(self.Dict)
        #print(self.List)
        if len(self.Dict[val]) == 0 : #If there are no indices remaining storing the val (ie empty set), we remove the entire item from the dictionary
            self.Dict.pop(val)
        return True #Return true since we successfully removed an item from the list

    def getRandom(self) -> int:
        return random.choice(self.List) #This line returns a random value from the list

def main():
    print("Read the following integers:")
    with open("input.txt") as f:
        lst = [int(x) for x in f.read().split()]
    #Using 'with' ensures the program doesn't get stuck if there is an I/O error, it's like an alternative to try/catch
    #f.read() returns a string, and split() returns a list of words
    #The way we've defined the list with a for loop is called 'list comprehension'
    print(lst)
    obj = RandomizedSet()
    obj2 = RandomizedCollection()
    #param_1 = obj.insert(val)
    #param_2 = obj.remove(val)
    #param_3 = obj.getRandom()
    #param_4 = obj2.insert(val)
    #param_5 = obj2.remove(val)
    #param_6 = obj2.getRandom()

if __name__ == "__main__": #Entry point
    main() #Calling main method