from collections import deque
from typing import Optional

#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/ (related)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #Note: This implementation works on any binary tree regardless of how the nodes are ordered. More efficiency might be possible
    #if we know the tree is a BST.
    #Also, this approach is inefficient due to us repeatedly creating new lists, which has linear complexity
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = []
        q_path = []
        queue = deque()
        if root:
            queue.append([root]) #Validation before appending to queue. We enqueue the entire path instead of individual nodes
        #Standard BFS/level order traversal where we record the entire path in the queue
        while queue:
            currPath = queue.popleft()
            currNode = currPath[-1]
            if currNode.val == p.val:
                p_path = currPath
                if q_path: break #Can stop if we have path for both p and q
            if currNode.val == q.val:
                q_path = currPath
                if p_path: break #Can stop if we have path for both p and q
            if currNode.left:
                queue.append(currPath + [currNode.left]) #Validate before enqueueing
            if currNode.right:
                queue.append(currPath + [currNode.right])

        p_set = set(p_path) #Make path of node p a set
        for node in q_path[::-1]: #Traverse q path backwards to go from lowest to highest
            if node in p_set: #The lowest node that is common in the path of q and p is the lowest common ancestor
                return node
        return None #This line will only be reached if there is no common ancestor
    


    #Much faster approach since we don't repeatedly create lists. This implementation is also for any binary tree, not tailored to a BST or any other specific type of tree.
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {} #Dictionary where the key is a node, and the value is its parent node. The root is not added as a key in this dictionary.
        queue = deque()
        if root:
            queue.append(root) #Validation while enqueing
        #Standard BFS/level order traversal
        while queue:
            currNode = queue.popleft()
            if p in parents and q in parents: #If we have found both p and q nodes, we can stop the traversal
                break
            if currNode.left:
                queue.append(currNode.left)
                parents[currNode.left] = currNode #Record the parent of this node
            if currNode.right:
                queue.append(currNode.right)
                parents[currNode.right] = currNode #Record the parent of this node

        p_set = set()
        p_set.add(p)
        currNode = p
        while currNode in parents:
            p_set.add(parents[currNode])
            currNode = parents[currNode]
        #p_set now contains all the nodes in the path going from the root to p
        currNode = q
        while currNode != root: #Iterate upwards from q by repeatedly accessing its parents, thus traversing the path from q to root
            if currNode in p_set: #The first node we encounter that is also in the p_set is the least common ancestor
                return currNode
            currNode = parents[currNode]
        
        return currNode


def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method