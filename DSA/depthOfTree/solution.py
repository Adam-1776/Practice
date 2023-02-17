from typing import Optional

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
    #Recursive solution
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None : #Terminal case
            return 0
        return max(1 + self.maxDepth(root.left) , 1 + self.maxDepth(root.right))


def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method