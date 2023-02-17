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
        def depth(node):
            if node == None : return 0 #Terminal case
            if node.left == None and node.right == None: return 1 #Terminal case where have found a leaf node
            leftDepth = depth(node.left)
            rightDepth = depth(node.right)
            if node.left == None : return 1 + rightDepth #If left child is absent, we know there must be a right child since we already checked for leaf node condition
            if node.right == None : return 1 + leftDepth #If right child is absent, we know there must be a left child
            return min(leftDepth + 1 , rightDepth + 1)

        return depth(root)


def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method