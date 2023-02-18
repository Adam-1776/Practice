from typing import Optional
#https://leetcode.com/problems/diameter-of-binary-tree/


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

#The diameter of a given subtree that starts from the root of that subtree is simply the sum of the heights of its
#left subtree and its right subtree. Therefore, we need to find the diameter of every node in the tree since the biggest
#diameter does not necessarily pass through the root of the tree.
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #This is actually a bottom-up solution. Since our recursion does not reach its terminal case until we reach a null node
        #Therefore, each node is only visited once, giving this O(n) time complexity
        def dfs(node): #Helper function to find the height of the tree that is rooted in parameter 'node'
            nonlocal biggestDiameter
            if node is None: #Terminal case
                return 0
            left = dfs(node.left) #Height of left subtree
            right = dfs(node.right) #Height of right subtree
            biggestDiameter = max(left + right, biggestDiameter) #diameter = height of left subtree + height of right subtree.
            #In the line above, we keep track of the biggest diameter we've encountered so far
            return max(left, right) + 1 #Height of the tree rooted in node is max(depth of left subtree, depth of right subtree) + 1

        biggestDiameter = 0
        dfs(root)
        return biggestDiameter

#Basically, this solution is very similar to the max depth of tree problem. Except we add an additional line to calculate the diameter and
#keep track of the biggest diameter seen so far.
def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method