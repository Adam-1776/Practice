from collections import deque
from math import inf
from typing import Optional

#https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level, levelSum = 1, float(-inf)
        queue = deque()
        currLevel = 1
        if root:
            queue.append(root)
        while queue:
            currentSum = 0
            for _ in range(len(queue)):
                currNode = queue.popleft()
                currentSum += currNode.val
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            if currentSum > levelSum:
                level, levelSum = currLevel, currentSum
            currLevel += 1
        return level

def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method