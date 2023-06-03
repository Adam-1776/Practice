from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:

    #Return node with val if it is present, else return None. It is recursive with no helper method.
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return None
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    #Insertion with recursion
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val) #If tree is empty, create a new root
        currNode = root
        def helper(currNode):
            if val < currNode.val: #Need to move left
                if currNode.left:
                    helper(currNode.left) #Recurse left
                else:
                    currNode.left = TreeNode(val) #If no left node is present, we've found insertion point
                    return
            elif val > currNode.val: #Need to move right
                if currNode.right:
                    helper(currNode.right) #Recurse right
                else:
                    currNode.right = TreeNode(val) #If no right node is present, we've found insertion point
                    return
            else: #Node with val is already in the tree
                return

        helper(currNode)
        return root
    
def main():
    print('No test case available')
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method