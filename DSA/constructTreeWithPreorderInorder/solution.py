from typing import Optional
#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


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
    #Inefficient solution due to no optimizations (repeatedly perform linear search on inorderlist and repeatedly construct new inorderlist and preorderlist, which have linear complexity)
    #The key idea is to create preorderList and inorderList such that they encompass, and only encompass, the subtree rooted in preorderList[0]
    #Since each preorderList and inorderList is created such that they are valid in their own right as their own tree, we can use a recursive helper method.
    #The way we create valid preorderList and inorderList for the left and right subtree for each node is to use the inorderList to see how many nodes are in the left and right
    #subtrees of currRoot. We call these numbers numLeft and numRight. We know preorderList[0] is the currNode, and the next numLeft nodes belong to the left subtree, and the
    #next numRight nodes after that belong to the right subtree. These subarrays are the preorderList for the left and right subtrees. Similarly for the inorderList, we know everything
    #up until the currNode belongs to the left subtree, and everything to the right of currNode belongs to the right subtree.
    #In this way, we have created the preorder and inorder lists that will be used to create the left and right subtrees. Again, the these inorder and preorder lists are completely
    #valid lists in their own right that are rooted in preorderList[0]. We don't need to deal with the fact that the currNode is in fact in the middle of the tree, we can treat
    #currNode like it's the root of a tree. We can do this since each node in a binary tree is the root of its own subtree, and the preorderList and inorderList we have computed are
    #specific to the subtree rooted in currNode. We can therefore proceed recursively.

    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:

        def helper(preorderList, inorderList): #The preorderList and inorderList are specific to the subtree rooted in preorderList[0]!
            if not preorderList or not inorderList: #Terminal case where the preorder or inorder lists are empty or invalid
                return None #Return a null node in this case
            #print(f'preorderList = {preorderList}')
            currRoot = TreeNode(preorderList[0]) #The first node in preorder is always the currRoot
            #print(f'currRoot = {currRoot.val}')
            inorderIndex = inorderList.index(currRoot.val) #Find the index in inorder here the currRoot is present
            numLeft = inorderIndex #There are numLeft elements to the left of the currRoot in the inorderList. These elements are in currNode's left subtree.
            numRight = len(inorderList) - inorderIndex - 1 #There are numRight elements to the right of currRoot in inorderList. These elements are in currNode's right subtree.
            #print(f'currRoot = {currRoot.val} and numLeft = {numLeft} and numRight = {numRight}')
            currRoot.left = helper(preorderList[1 : 1+numLeft], inorderList[:inorderIndex]) #Construct new preorderList and inorderList for the left subtree accordingly
            currRoot.right = helper(preorderList[1+numLeft : 1+numLeft+numRight], inorderList[inorderIndex + 1:]) #Construct new preorderList and new inorderList for the right subtree
            return currRoot

        return helper(preorder, inorder)


def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method