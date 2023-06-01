from typing import Optional

#https://leetcode.com/problems/path-sum/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
    def printList(self) :
        cur = self
        numstr = ""
        while cur :
            numstr += str(cur.val) + " "
            cur = cur.next
        print(numstr)
def createList(nums: list[int]) -> ListNode :
    if len(nums) < 1 : return None
    cur = ListNode(nums[0])
    head = cur
    for i in range(1,len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return head
"""

class Solution:
    #Note that the sum must be reached at a leaf node, not in the middle of the tree!
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #This helper method basically does preorder DFS traversal
        def hasPathHelper(node, sum):
            if node == None : return False #Terminal case: if there was a solution in this path it would have been found already
            sum += node.val #Add current node to the sum so far
            if sum == targetSum and node.left == None and node.right == None : return True #Positive terminal case
            return hasPathHelper(node.left, sum) or hasPathHelper(node.right, sum) #Recursion. Check if either of the subtrees can find a valid path to target

        if not root : return False
        return hasPathHelper(root, 0)

    #This implementation also prints the path that adds up to the targetSum, if such a path is found
    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def hasPathHelper(node, sum, path):
            if node == None :
                del path
                return False
            sum += node.val
            path.append(node.val)
            if sum == targetSum and node.left == None and node.right == None : 
                print(path)
                return True
            #In the line below, we have to pass a copy of the list, not the list itself. This is so that each recursion will have a unique copy of the list
            #instead of multiple recursion paths adding to the same list.
            return hasPathHelper(node.left, sum, path.copy()) or hasPathHelper(node.right, sum, path.copy())

        if not root : return False
        pathList = []
        return hasPathHelper(root, 0, pathList)

    #Below implmentation stores a list of node pointers that make up the path we're looking for
    def hasPathSum3(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def hasPathHelper(node, sum, path):
            if node == None :
                del path
                return False
            sum += node.val
            path.append(node) #Append a pointer to the curret node
            if sum == targetSum and node.left == None and node.right == None : 
                nonlocal pathList #Use nonlocal keyword so that we are using the pathList variable in the hasPathSum3 method
                pathList = path #Assign the current path list to pathList
                return True
            return hasPathHelper(node.left, sum, path.copy()) or hasPathHelper(node.right, sum, path.copy())

        if not root : return False
        pathList = []
        if hasPathHelper(root, 0, pathList) == True:
            for node in pathList: #The pathList variable now has a list of pointers to the nodes in the path
                print(node.val)
            return True
        else: return False

    #Plain DFS implementation
    def hasPathSum4(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        stack = []
        stack.append([root, root.val]) #Stack contains the [currentRoot, totalSumOnThisPathSoFar]

        while stack:
            currTraversal = stack.pop()
            currNode, currSum = currTraversal[0], currTraversal[1]
            if currNode.left == None and currNode.right == None and currSum == targetSum: #If currNode is a leaf node
                return True
            if currNode.left:
                stack.append([currNode.left, currSum + currNode.left.val])
            if currNode.right:
                stack.append([currNode.right, currSum + currNode.right.val])
            
        return False

    #Plain DFS that also stores the path
    def hasPathSum5(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        stack = []
        stack.append([[root], root.val]) #Stack contains the [[currentPath], totalSumOnThisPathSoFar]

        while stack:
            currTraversal = stack.pop()
            #Current node is the last node in the list. We don't need to store the currSum since we can compute currSum
            #in each traversal by adding up all the nodes in the path, but we store it for efficiency.
            #Note that currPath is a list of node pointers, not their values
            currPath, currNode, currSum = currTraversal[0], currTraversal[0][-1], currTraversal[1]
            if currNode.left == None and currNode.right == None and currSum == targetSum: #If currNode is a leaf node
                print(f'Path is {[i.val for i in currPath]}') #List comprehension to get all values in currPath
                return True
            if currNode.left: #Only valid neighbors are added to the stack, so we don't need to validate the currNode in each iteration
                stack.append([currPath + [currNode.left], currSum + currNode.left.val])
            if currNode.right:
                stack.append([currPath + [currNode.right], currSum + currNode.right.val])
            
        return False

def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method