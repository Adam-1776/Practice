from typing import Optional
from collections import deque
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
    #Inorder is handy on BST because it prints all the nodes in ascending order
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        traversal = []

        def inorderHelper(node):
            if node == None: return #Only stop when we hit None (meaning the node that invoked this call of the method is a leaf node)
            inorderHelper(node.left)
            traversal.append(node.val) #Only append when we've fully traversed left child tree recursively
            inorderHelper(node.right)

        inorderHelper(root)
        return traversal


    #Iterative in order traversal using stack. This can be handy in certain problems such as finding kth smallest element in a BST
    def inorderTraversal2(self, root: Optional[TreeNode]) -> list[int]:
        traversal = []
        stack = []
        currNode = root
        while currNode or stack:
            if currNode: #We try to move down and to the left as our 'first preference' if currNode is valid
                stack.append(currNode) #Add this node to the stack since we haven't traversed it's right subtree yet
                currNode = currNode.left
            else: #If we are in a null node, have no choice but to backtrack up by popping from the stack.
                currNode = stack.pop() #We pop the 'lowest' node who's left subtree is exhausted
                traversal.append(currNode.val) #We print the node before moving to its right subtree
                currNode = currNode.right
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



    #Preorder using iterative DFS with stack.
    def preorderTraversal2(self, root: Optional[TreeNode]) -> list[int]:
        traversalList = []
        stack = []
        if root: stack.append(root) #In this case, we choose to validate while appending to stack
        #Alternatively, we could also blindy append to stack and only validate while popping. That also works.
        while stack:
            currNode = stack.pop()
            traversalList.append(currNode.val)
            if currNode.right: stack.append(currNode.right) #Notice how we add the right child first to emulate left recursion
            if currNode.left: stack.append(currNode.left)
        return traversalList



    #Level order is  basically a plain BFS traversal.
    def levelOrder(self, root: Optional[TreeNode]) -> list[int]:
        queue = deque()
        queue.append(root)
        traversal = []
        while queue:
            currNode = queue.popleft()
            if not currNode: continue #Need to validate here, since we don't validate when adding to queue
            traversal.append(currNode.val)
            #Below, we add neighbors of currNode to the queue
            queue.append(currNode.left)
            queue.append(currNode.right)
        return traversal

    #This level order implementation returns a 2D list, with each level of nodes in a seperate row
    def levelOrder2(self, root: Optional[TreeNode]) -> list[list[int]]:
        queue = deque()
        if root: queue.append(root) #Need to perform validation upfront
        #Note: we do validation when appending to queue because we do not want any null nodes in the queue.
        traversal = []
        while queue:
            traversal.append([])
            for _ in range(len(queue)): #We use the inner loop trick to count each level or 'layer' of the traversal seperately. Have to do this since each node has multiple unvisited neighbors
                currNode = queue.popleft()
                #No need to validate currNode, since we only enqueue valid nodes
                traversal[-1].append(currNode.val) #Append this node to the latest row in traversal
                #Below, we add valid neighbors of currNode to the queue.
                if currNode.left: queue.append(currNode.left)
                if currNode.right: queue.append(currNode.right)
        return traversal


def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method