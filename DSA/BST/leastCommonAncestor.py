from collections import deque

#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solutions/1347857/c-java-python-iterate-in-bst-picture-explain-time-o-h-space-o-1/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    #This approach takes advantage of the way BSTs are structured. If a node's value is in between p and q, then that node
    #must be the lowest common ancestor since p will be to its left and q will be to its right
    #In other cases, p or q will be the other's lowest common ancestor one's path to the tree will be a subarray of the other's path to the tree
    #For example if p is above q, then p is q's LCA. If q is above p, then q is p's LCA. 
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val: #We want p to be smaller for simplicity
            p, q = q, p
        stack = []
        if root: stack.append(root) #Validation before pushing to stack
        #Perform a standard DFS traversal of the tree
        while stack:
            currNode = stack.pop()
            if currNode.val > p.val and currNode.val < q.val: #currNode must be their LCA since p is to its left and q is to its right
                return currNode
            if currNode.val == p.val or currNode.val == q.val: #If currNode is p, then it is q's LCA. If currNode is q, then it is p's LCA
                return currNode
            if currNode.right: stack.append(currNode.right) #only push valid children to stack
            if currNode.left: stack.append(currNode.left)
        return None
    

    #Better approach with O(log(n)) time if the tree is balanced. In this case we basically traverse the BST
    #searching for p or q. If we run into either p or q, it is the LCA. If we find a node that lies in between p and q
    #We know this node is their LCA.
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val: #We want p to be smaller for simplicity
            p, q = q, p
        currNode = root
        while currNode:
            if currNode.val > p.val and currNode.val < q.val:
                return currNode
            if currNode.val == p.val or currNode.val == q.val:
                return currNode
            if currNode.val > p.val:
                currNode = currNode.left
            else:
                currNode = currNode.right
        return currNode 




def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method