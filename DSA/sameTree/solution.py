from typing import Optional

#https://leetcode.com/problems/same-tree/


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
    #Two trees are identical if three conditions are met: same head node, same left subtree, and same right subtree
    #This makes this problem ripe for a recursive solution
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSameNode(p,q):
            if p == None and q == None : return True
            if p == None or q == None : return False
            return p.val == q.val

        if not isSameNode(p,q) : return False #If both roots are different, return False
        if p == None and q == None : return True #If both roots are None, return True
        return self.isSameTree(p.left ,q.left) and self.isSameTree(p.right ,q.right)


def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method