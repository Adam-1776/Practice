from typing import Optional

#https://leetcode.com/problems/symmetric-tree/


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
    #Somewhat similar to the same tree problem, but have to be more clever
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetricNodes(leftRoot, rightRoot): #This helper function is recursive
            if leftRoot == None and rightRoot == None : return True #Terminal Case
            if leftRoot == None or rightRoot == None : return False #Terminal Case
            if leftRoot.val != rightRoot.val : return False #Terminal Case
            #If none of the terminal cases above are applicable, then make a recursive call below:
            return symmetricNodes(leftRoot.left , rightRoot.right) and symmetricNodes(leftRoot.right, rightRoot.left)

        if root : return symmetricNodes(root.left, root.right)
        else : return True


def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method