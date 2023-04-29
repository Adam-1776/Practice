from typing import Optional

#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
#Note: There can be more than possible tree that fits the solution

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

        #Helper function to find height of tree. If there is an imbalance of more than one for any subtree, return -1
        def depth(root):
            if root == None : return 0
            leftHeight = depth(root.left) #Need to record the depth of the subtree for each node this recursive function is called upon
            rightHeight = depth(root.right)
            if leftHeight == -1 or rightHeight == -1 : return -1 #If any of the subtrees at any call to this recursive function is imbalanced, exit immediately
            if abs(leftHeight - rightHeight) > 1 : return -1
            return max(1 + leftHeight, 1 + rightHeight)

        if root == None : return True
        return depth(root) != -1


def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method