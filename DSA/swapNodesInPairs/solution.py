from typing import Optional

#https://leetcode.com/problems/swap-nodes-in-pairs/


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
    #The trick to this problem is understanding the dance of pointers that takes place
    #between prevNode, currNode, and nextNode. prevNode points to currNode's next
    #currNode points to nextNode's next, and nextNode points to currNode
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head) #Insert dummy node before head
        currNode = head #Start currNode from head
        prevNode = dummy #Start prevNode before currNode, which is the dummy node

        while currNode:
            nextNode = currNode.next
            if nextNode: #If nextNode exists
                currNode.next = nextNode.next #currNode now points to the node two places ahead
                nextNode.next = currNode #The original nextNode now points to currNode
                prevNode.next = nextNode #prevNode now points to the node that was originally two places ahead of it
            prevNode = currNode
            currNode = currNode.next #Notice that if we performed swapping above, we have actually moved two spaces forward in the linked list since
                                     #currNode itself has moved forward. If we didn't perform swapping we've only moved once place forward in the linked list
        
        return dummy.next


def main():
    print('No test case')
    #Check if a linked list has any cycles. In other words, does any node have a next pointer that goes 'backwards' to a previous node.
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method