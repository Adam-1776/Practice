#https://leetcode.com/problems/validate-binary-search-tree/

from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #The key to this problem is that not only does the left child have to be smaller and the right child greater for a given node,
    #the ENTIRE left SUBTREE has to be smaller and the ENTIRE right SUBTREE has to be bigger! Even if each parent-children pair are compliant, if
    #there is a value later down in the left subtree that is bigger or down in the right subtree that is smaller, it's not a valid BST.
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def bstHelper(currNode, lowerBound, upperBound): #Helper method that checks if currNode is within limits of lower and upper bounds
            if not currNode: #No compliance problem if invalid node
                return True
            if currNode.val <= lowerBound or currNode.val >= upperBound: #If node is out of bounds, return false
                return False
            if not bstHelper(currNode.left, lowerBound, currNode.val): #The left subtree must be smaller than currentNode, and it inherits its lower bound
                return False #Note that lowerBound only changes when we move to a right child
            if not bstHelper(currNode.right, currNode.val, upperBound): #The right subtree must be bigger than currentNode, and it inherits its upper bound
                return False #Note that upperBound only changes when we move to a left child
            #As we traverse down the tree, the lower and upper bounds are inherited as necessary from parent nodes. This is to make sure entire subtrees are compliant
            #Need to do it this way since the child nodes can have the same limits as its parent in case of a 'zig zag' movement. For example if a node is right of the root,
            #and its child is to its left. The child inherits its parent's restriction to be greater than the root.
            return True

        return bstHelper(root, float(-inf), float(inf)) #The root node has no restrictions on its minimum or maximum value
    


    #This implementation takes advantage of the fact that an inorder traversal of a valid BST prints nodes in strictly increasing order.
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        currNode = root
        prevNode = None #This node holds the latest node that would have been 'printed' or 'marked' in an inorder traversal
        stack = []
        #Perform an interative inorder traversal
        while currNode or stack:
            if currNode:
                stack.append(currNode)
                currNode = currNode.left
            else:
                currNode = stack.pop()
                if prevNode and prevNode.val >= currNode.val: #If the current node isn't bigger than the last node that was printed, not a valid BST
                    return False
                prevNode = currNode #We would have printed currNode at this point. So set prevNode to equal currNode and continue
                currNode = currNode.right
        return True
    
def main():
    print('No test case available')
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method