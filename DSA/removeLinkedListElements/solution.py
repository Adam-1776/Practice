from typing import Optional

#https://leetcode.com/problems/remove-linked-list-elements/

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
    #Using a dummy node works well for this problem since it alleviates us of the edge case of changing the head
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyNode = ListNode(-1,head) #Add a dummy node before the head of the list
        currNode = dummyNode
        #We check the value in front of currNode instead of currNode itself, since if we find a node that needs to be removed,
        #we have to modify the node behind the unwanted node, not the unwanted node itself!
        while currNode.next: #Keep iterating up until currNode is the second last Node in the list
            if currNode.next.val == val: #Check the value of the node in front of currNode
                currNode.next = currNode.next.next #Skip the unwanted node by setting the next pointer accordingly
            else: #Important: We use an else statement since we do not want to increment currNode if we just removed the node ahead!
                currNode = currNode.next
        return dummyNode.next


def main():
    linkedList1 = createList([1,2,6,6,6,3,3,5,6,7,6])
    solution = Solution()
    newLinkedList1 = solution.removeElements(linkedList1, 6)
    newLinkedList1.printList()
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method