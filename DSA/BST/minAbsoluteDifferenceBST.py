#https://leetcode.com/problems/minimum-absolute-difference-in-bst/

from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #Need to traverse all the nodes to find which two have the minimum absolute difference
    #Perform an in-order traversal, taking advantage of the fact that in-order traversal of BST prints in ascending order
    #Therefore, the two nodes that form the minimum absolute difference must be traversed consecutively in an in-order traversal
    #O(n) time complexity and O(log(n)) space complexity due to the stack used for inorder traversal. Might be able to reduce space with a morris inorder traversal
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        lastNode = None #The last node that would have printed in the inorder traversal
        minDifference = float(inf)
        stack = []
        currNode = root
        #Iterative in-order traversal
        while currNode or stack:
            if currNode:
                stack.append(currNode)
                currNode = currNode.left
            else:
                currNode = stack.pop()
                if lastNode: #Compare the currNode to the lastNode. If their difference is the minimum found so far, update minDifference
                    minDifference = min(abs(lastNode.val - currNode.val), minDifference) #Note, we could do without the abs() function since we know currNode is always bigger than lastNode
                lastNode = currNode
                currNode = currNode.right

        return minDifference
    



    #Note: this does NOT work!! Wrote this with the INCORRECT assumption that the min difference will always be between a parent and child pair of nodes
    def getMinimumDifferenceWrong(self, root: Optional[TreeNode]) -> int:
        minDifference = 9999

        def preorder(currNode):
            nonlocal minDifference
            if currNode.left:
                minDifference = min(abs(currNode.val - currNode.left.val), minDifference)
                preorder(currNode.left)
            if currNode.right:
                minDifference = min(abs(currNode.val - currNode.right.val), minDifference)
                preorder(currNode.right)

        preorder(root)
        return minDifference



#Note: If the tree was not a BST. The approach would be to do any traversal and append all the values in a list.
#Then, sort the list. Then traverse the list to find the adjacent elements with the smallest difference. This approach would have nlog(n) complexity
def main():
    print('No test case available')
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method