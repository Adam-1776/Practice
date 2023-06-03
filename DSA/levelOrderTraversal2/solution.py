#https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

from collections import deque
from typing import Optional

# Definition for a Node.
class TreeNode:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    #Same approach as BFS with 2D list, except we add a new row to the beginning of our 2D list.
    def levelOrderBottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        queue = deque()
        traversal = deque() #Use deque since we will appending to the left
        if root: queue.append(root)
        while queue:
            traversal.appendleft([])
            for _ in range(len(queue)):
                currNode = queue.popleft()
                traversal[0].append(currNode.val) #We are always in the leftmost row in traversal
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
        return list(traversal)



def main():
    print(f'No test case available here')
    
    
if __name__ == "__main__": #Entry point
    main() #Calling main method