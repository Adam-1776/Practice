from typing import Optional

#https://leetcode.com/problems/balanced-binary-tree/

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
    #The trick is to check ALL the nodes to see if their subtree is balanced. It is not enough to just see if the subtrees of the root are balanced!
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        #This helper function returns depth of subtree rooted in currNode. If it's imbalanced, it returns -1
        #Notice how the return integer conveys two pieces of information: depth as well as its height
        #We can do this since if the subtree is imbalanced, then we don't need its height.
        def depth(currNode):
            if not currNode: return 0 #Terminal case: this subtree is balanced but zero height
            leftHeight = depth(currNode.left)
            rightHeight = depth(currNode.right)
            if leftHeight == -1 or rightHeight == -1: #If either child is imbalanced, this subtree is imbalanced 
                return -1
            if abs(leftHeight - rightHeight) > 1: #If children subtrees are balanced but have much different heights...
                return -1 #Then this subtree is imbalanced. Terminate here.
            return 1 + max(leftHeight, rightHeight)

        return depth(root) != -1

def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method