#https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #Take advantage of the fact that an inorder traversal of a valid BST prints the nodes in strictly increasing order
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        currNode = root
        numNodesTraversed = 0 #Number of nodes that we would have printed during this inorder traversal (though we aren't actually printing)
        #Perform an iterative inorder traversal
        while stack or currNode:
            if currNode:
                stack.append(currNode)
                currNode = currNode.left
            else:
                currNode = stack.pop()
                numNodesTraversed += 1 #We would have printed at this point, since we've exhausted currNode's left subtree and are about to enter it's right
                if numNodesTraversed == k: #If we would have printed the kth node at this point, it is the kth smallest node
                    return currNode.val #We found our value, return it
                currNode = currNode.right
        return None #This line will only be rached if the BST has fewer than k nodes
    
def main():
    print('No test case available')
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method