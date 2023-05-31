from typing import Optional
from collections import deque

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
    #Somewhat similar to the same tree problem, but have to be more clever. Recursive solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        #This helper method assumes that everything above leftRoot and rightRoot is symmetric
        def symmetricNodes(leftRoot, rightRoot): #This helper function is recursive
            if leftRoot == None and rightRoot == None : return True #Terminal Case
            if leftRoot == None or rightRoot == None : return False #Terminal Case
            if leftRoot.val != rightRoot.val : return False #Terminal Case
            #If none of the terminal cases above are applicable, then make a recursive call below:
            return symmetricNodes(leftRoot.left , rightRoot.right) and symmetricNodes(leftRoot.right, rightRoot.left)

        if root : return symmetricNodes(root.left, root.right)
        else : return True

    #Iterative approach
    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        q = deque() #Use a queue since this is a type of BFS
        q.append(root.left)
        q.append(root.right)
        while q:
            l = q.popleft()
            r = q.popleft()
            #The front two nodes in the queue are the ones that need to be compared
            if l == None and r == None: #Positive terminal case, can skip this iteration
                continue
            if l == None or r == None or l.val != r.val: #Negative terminal case, can return False immediately
                return False
            #The below lines are key. We add nodes in order such that two nodes that should be equal will be right next to each other in the queue.
            #That way when we deque two nodes in the next iteration, those two nodes should be equal.
            q.append(l.left)
            q.append(r.right)
            q.append(l.right)
            q.append(r.left)
        
        return True


def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method