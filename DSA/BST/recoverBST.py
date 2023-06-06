from collections import deque
from typing import Optional

#https://leetcode.com/problems/recover-binary-search-tree/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        foundNodes = [] #List of nodes that are out of order when doing inorder traversal
        stack = []
        prevNode = None #Last node that would have been printed in the inorder traversal
        currNode = root
        #Perform an inorder traversal iteratively (recursive would also work)
        while currNode or stack:
            if currNode:
                stack.append(currNode)
                currNode = currNode.left
            else:
                currNode = stack.pop()
                if prevNode and currNode.val <= prevNode.val: #If this node is not bigger than prevNode...
                    foundNodes.append(currNode)
                    foundNodes.append(prevNode) #Add then to our foundNodes list
                prevNode = currNode
                currNode = currNode.right
        
        #print(f'{[node.val for node in foundNodes]}')
        #foundNodes will have either 2 or 4 values assuming only one pair of nodes has to be swapped. Swap their values only to keep structure intact.
        if len(foundNodes) == 2:
            foundNodes[0].val, foundNodes[1].val = foundNodes[1].val, foundNodes[0].val
        elif len(foundNodes) == 4:
            foundNodes[1].val, foundNodes[2].val = foundNodes[2].val, foundNodes[1].val




def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method