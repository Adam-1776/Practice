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
        #This is a normal BFS level order traversal for the most part
        while queue:
            levelQueue = deque() #This queue will store the nodes found in this level. Use queue for efficiency in case we need to store in reverse order
            for _ in range(len(queue)): #Inner loop to keep track of level. Necessary because each node has multiple unvisited neighbors
                currNode = queue.popleft()
                levelQueue.appendleft(currNode.val)
                if currNode.left: queue.append(currNode.left)
                if currNode.right: queue.append(currNode.right)
            if level % 2 == 1: result.append(list(levelQueue)) #If level is odd, convert the queue to a list and append it to our 2D list
            else: result.append(list(reversed(levelQueue))) #If level is even, reverse the queue, convert to a list and append it to our 2D list
            level += 1
        return result


def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method