from typing import Optional

#https://leetcode.com/problems/reverse-linked-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

class Solution:
    #Simple approach with O(n) space complexity, since we store pointers to all the nodes
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head : return None
        nodeList = []
        while head:
            nodeList.append(head)
            head = head.next
        #nodeList now has a list of pointers to the nodes in their original order
        for i in range(len(nodeList) - 1, 0, -1): #Traverse the list backwards till the the second element
            nodeList[i].next = nodeList[i-1]
        nodeList[0].next = None #The first element in the list (tail node in the new linked list) needs its next pointer set
        return nodeList[-1] #Return the new head of the reversed linked list

    #Approach with O(1) space complexity
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #keep track of two nodes: the current node and the node behind current node
        #In the loop we also get the next node, so we are actually tracking three nodes.
        currNode = head #Start off current node as head
        prevNode = None #The node behind current node is None (since the currNode is the head right now)
        while currNode: #Keep going till currentNode has reached the end
            nextNode = currNode.next #Record the node ahead
            currNode.next = prevNode #currNode should now point to its previous node
            prevNode = currNode #Move prevNode forward
            currNode = nextNode #Move currNode forward
        #At the end of the loop, currNode will be None and prevNode will be the new head
        #This is because the tail of the original list will be the head of the new list.
        #At the end of the loop, currNode will be beyond the tail of the original list, and prevNode will be the tail of the original list
        return prevNode


def main():
    solution = Solution()
    list1 = [1,2,3,4,5,6,7,8]
    head1 = createList(list1)
    head2 = solution.reverseList(head1)
    head2.printList()
    
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method