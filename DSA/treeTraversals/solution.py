from typing import Optional
#https://leetcode.com/problems/binary-tree-postorder-traversal/
#https://leetcode.com/problems/binary-tree-inorder-traversal/
#https://leetcode.com/problems/binary-tree-preorder-traversal/


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
    #Postorder is a type of DFS. The nodes recorded in traversal[] are not really the honest in order in which we visited the nodes. They're actually recorded in
    #backwards order for the left subtree, then the right subtree
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        traversalList = []

        def traversalHelper(node):
            if not node : return #Only stop when we hit None (meaning the node that invoked this call of the method is a leaf node)
            traversalHelper(node.left)
            traversalHelper(node.right)
            traversalList.append(node.val) #Only append this node when we have fully traversed both child trees recursively

        traversalHelper(root)
        return traversalList

    #Inorder is a type of DFS. The nodes recorded in traversal[] are not really the honest in order in which we visited the nodes. They're actually recorded in
    #backwards order for the left subtree, then the root is recorded, and then the right subtrees.
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        traversal = []

        def inorderHelper(node):
            if node == None: return #Only stop when we hit None (meaning the node that invoked this call of the method is a leaf node)
            inorderHelper(node.left)
            traversal.append(node.val) #Only append when we've fully traversed left child tree recursively
            inorderHelper(node.right)

        inorderHelper(root)
        return traversal
    
    #Preorder is a plain DFS with left recursion. The traversal[] list honestly records the order in which we visited the nodes in the graph.
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        traversalList = []

        def traversalHelper(node):
            if not node : return #Only stop when we hit None (meaning the node that invoked this call of the method is a leaf node)
            traversalList.append(node.val)
            traversalHelper(node.left)
            traversalHelper(node.right)

        traversalHelper(root)
        return traversalList


def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method