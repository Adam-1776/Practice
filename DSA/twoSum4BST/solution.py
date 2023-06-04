from typing import Optional

#https://leetcode.com/problems/two-sum-iv-input-is-a-bst/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #The fact that the tree is a BST isn't relevant in this implementation, it works on any binary tree. A more efficient approach
    #may be possible by tailoring our implementation to a BST.
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        foundNodes = set()
        def dfs(currNode):
            if not currNode: return False #Terminal case, no matching nodes found
            if (k - currNode.val) in foundNodes: #Terminal case, matching nodes found
                return True
            foundNodes.add(currNode.val)
            #print(f'Added {currNode.val}')
            return dfs(currNode.left) or dfs(currNode.right) #Recursive case, if match is found in EITHER left or right subtree, True is returned

        return dfs(root)


def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method