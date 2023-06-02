from typing import Optional
#https://leetcode.com/problems/minimum-depth-of-binary-tree/
#https://leetcode.com/problems/maximum-depth-of-binary-tree/


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
    #Recursive solution for depth of tree
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None : #Terminal case
            return 0
        return max(1 + self.maxDepth(root.left) , 1 + self.maxDepth(root.right))

    #Recursive solution for minimum depth between root and any leaf node
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #This problem is tricker than max depth of tree!
        #We cannot simply stop at a 'None' node, since the parent of this 'None' node may not be a leaf node, have to be more careful
        #Notice how we don't explicitly store the depht of the current node. We implicitly know since we add one to each recursive call we make
        def depth(node):
            if node == None : return 0 #Terminal case
            if node.left == None and node.right == None: return 1 #Terminal case where have found a leaf node
            leftDepth = depth(node.left)
            rightDepth = depth(node.right)
            #In the lines below, we add one to account for the current node!
            if node.left == None : return 1 + rightDepth #If left child is absent, we know there must be a right child since we already checked for leaf node condition
            if node.right == None : return 1 + leftDepth #If right child is absent, we know there must be a left child
            return min(leftDepth + 1 , rightDepth + 1)

        return depth(root)


    #More concise approach to minDepth (this is probably the best approach)
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #Helper method to find the minimum depth of a subtree rooted in currNode
        def depthHelper(currNode):
            #Don't need to check if currNode is None, since we check before calling the method in the first place.
            if not currNode.left and not currNode.right: #Terminal case, subtree has height one since it is a leaf
                return 1
            #Height of tree in non-terminal cases rooted in currNode is 1 + height of its shortest child subtree
            if not currNode.left: #If only right node is present
                return 1 + depthHelper(currNode.right)
            if not currNode.right: #If only left node is present
                return 1 + depthHelper(currNode.left)
            #If both child nodes are present
            return 1 + min(depthHelper(currNode.left), depthHelper(currNode.right))
        return depthHelper(root) if root else 0

    
    #More concise approach to minDepth, but in this approach we call recursion on both childs blindly without checking if it's valid first.
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def dfsHelper(currNode, currDepth):
            if not currNode:
                return 999999 #We don't know whether the parent is a leaf or not. This value will be eliminated anyway if a leaf is found in an earlier recursion
                               #You can think of it like backtracking since we want to cancel the affect of reaching a None node.
            currDepth += 1
            if not currNode.left and not currNode.right:
                return currDepth
            return min(dfsHelper(currNode.left, currDepth), dfsHelper(currNode.right, currDepth))
        return dfsHelper(root, 0)


def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method