from typing import Optional

#https://leetcode.com/problems/remove-nth-node-from-end-of-list/


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
    #This solution performs deletion in a single pass
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) #Insert dummy node before the head
        fastNode = head
        for _ in range(n):
            fastNode = fastNode.next
        #We have now moved the fastNode so that it is n spaces ahead of the head
        currNode = head
        prevNode = dummy
        #From here on out, currNode will always be two spaces behind fastNode. This allows us to find the nth node from the end without backtracking or using memory
        while fastNode: #Keep going till fastNode is beyond the tail and therefore equals null
            fastNode = fastNode.next
            currNode = currNode.next
            prevNode = prevNode.next
        #By now, currNode is the node that needs to be deleted, and prevNode is the node right behind it
        prevNode.next = currNode.next
        return dummy.next


def main():
    print('No test case')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method