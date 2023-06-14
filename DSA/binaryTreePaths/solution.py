from collections import deque
from typing import Optional

#https://leetcode.com/problems/binary-tree-paths/

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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        result = []
        queue = deque()
        if root:
            queue.append([root, str(root.val)]) #Validation before enqueueing
        #Just a standard BFS traversal
        while queue:
            curr = queue.popleft()
            currNode, currPath = curr[0], curr[1]
            if not currNode.left and not currNode.right:
                result.append(currPath)
                continue
            if currNode.left:
                queue.append([currNode.left, str(currPath + "->" + str(currNode.left.val))])
            if currNode.right:
                queue.append([currNode.right, str(currPath + "->" + str(currNode.right.val))])
        return result

def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method