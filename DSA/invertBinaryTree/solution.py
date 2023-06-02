from typing import Optional

#https://leetcode.com/problems/invert-binary-tree/


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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertHelper(node):
            if node == None : return None #Terminal case
            node.left, node.right = node.right, node.left #Swap left and right nodes (works regardless of None pointers, this will work)
            invertHelper(node.left) #Recursive calls
            invertHelper(node.right)
        invertHelper(root)
        return root
    
    #Approach without helper method
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root #Terminal case
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method