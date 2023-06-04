from collections import deque

#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/ (this solution also works for this problem, albeit not the most efficiently)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #Note: This implementation works on any binary tree regardless of how the nodes are ordered. More efficiency is possible
    #if we know the tree is a BST since we can then predict the locations of p and q based on the current node's value
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
    #It also takes into account the case of either p or q not being in the tree. In that case, None will be returned.
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent  = {} #Key is node, value is it's parent
        queue = deque()
        if root:
            queue.append(root) #Validation while enqueing
            parent[root] = None #Parent of root set to None
        while queue:
            currNode = queue.popleft()
            if p in parent and q in parent: #If we have found both p and q nodes, we can stop the traversal
                break
            if currNode.left:
                queue.append(currNode.left)
                parent[currNode.left] = currNode #Record the parent of this node
            if currNode.right:
                queue.append(currNode.right)
                parent[currNode.right] = currNode #Record the parent of this node

        p_set = set()
        p_set.add(p)
        currNode = p
        while currNode in parent:
            p_set.add(parent[currNode])
            currNode = parent[currNode]
        #p_set now contains all the nodes in the path going from p to root including None at the top
        currNode = q
        while currNode != None: #Iterate upwards from q by repeatedly accessing its parents, thus traversing the path from q to root
            if currNode in p_set: #The first node we encounter that is also in the p_set is the lowest common ancestor
                return currNode #Return the lowest ancestor that we found
            currNode = parent[currNode]
        
        return currNode #If this line is reached, currNode is None and no common ancestor exists because p or q not in the tree




    #Very clever recursive approach, but does not take into account the case of p or q not in the tree
    def lowestCommonAncestor4(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if root in (None, p, q): return root #Terminal case, p or q is the root
            left = self.lowestCommonAncestor4(root.left, p, q)
            right = self.lowestCommonAncestor4(root.right, p, q)
            
            if not left and not right: return None; 
            if left and right: return root
            if not left:
                return right
            else:
                return left
        

def main():
    print('No test case available')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method