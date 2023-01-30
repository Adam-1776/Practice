from typing import Optional

#https://leetcode.com/problems/linked-list-cycle/


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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set() #Set of all node addresses we've seen
        while head:
            if id(head) in seen : return True #We've seen this address before, so there must be a cycle
            seen.add(id(head))
            head = head.next
        return False #If we reach the end of the list, there is no cycle


def main():
    print('No test case')
    #Check if a linked list has any cycles. In other words, does any node have a next pointer that goes 'backwards' to a previous node.
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method