from collections import deque
from typing import Optional

#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


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

    #This one works reasonably efficiently. Basically a standard BFS level order traversal,
    #but we keep track of the level and append the nodes of that level in reverse order if the level number is odd
    def zigzagLevelOrder2(self, root: Optional[TreeNode]) -> list[list[int]]:
        queue = deque()
        if root: queue.append(root)
        result = []
        level = 0
        while queue:
            levelQueue = deque() #This queue will store the nodes found in this level. Use queue for efficiency in case we need to store in reverse order
            for _ in range(len(queue)):
                currNode = queue.popleft()
                #print(f'currNode = {currNode.val} and level = {level}')
                if level % 2 == 1: #print the level right to left if we are on an odd level
                    levelQueue.appendleft(currNode.val)
                else:
                    levelQueue.append(currNode.val)
                if currNode.left: queue.append(currNode.left)
                if currNode.right: queue.append(currNode.right)
            result.append(list(levelQueue))
            level += 1
        return result


def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method