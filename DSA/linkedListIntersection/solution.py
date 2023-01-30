from typing import Optional

#https://leetcode.com/problems/intersection-of-two-linked-lists/


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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seenNodes = set()
        while headA :
            seenNodes.add(id(headA)) #Add all the nodes in headA to our set
            headA = headA.next
        while headB :
            if id(headB) in seenNodes : return headB #The first node in headB that has been seen in headA is our intersection point
            headB = headB.next
        return None #If we've gotten here, there's no intersection


def main():
    print('No test case')
    #Determine where two linked lists intersect. At some point, both linked lists will both point to a single node and thus merge going forward.
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method