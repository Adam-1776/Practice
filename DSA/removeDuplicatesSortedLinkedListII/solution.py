from typing import Optional

#https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/


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
    #A bit verbose but works
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        dummyNode = ListNode(0, head) #Dummy node is behind the head
        currNode = head #Start with the head
        prevNode = dummyNode #The dummy node is behind the head
        while currNode:
            nextNode = currNode.next
            if nextNode and nextNode.val == currNode.val: #We found duplicates. Need to delete currNode, nextNode, and further nodes that are equivalent
                while nextNode and nextNode.val == currNode.val:
                    nextNode = nextNode.next
                #After the above loop, nextNode points to the first node that is no longer equal to currNode
                prevNode.next = nextNode #prevNode now points to nextNode, skipping all nodes that were equal to currNode
                currNode = nextNode #We have a new currNode
                #Notice how we do not update prevNode inside this if-block, since we have made a deletion. This is a common pattern when performing deletions in linked lists
            #The below else statement does not execute if we entered the if-block and performed deletions
            else: #If there is no duplicate right now...
                prevNode = currNode #Update prevNode
                currNode = currNode.next #Move prevNode and currNode normally

        return dummyNode.next
    
    #Another approach
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        dummyNode = ListNode(0, head)
        currNode = head
        prevNode = dummyNode
        while currNode:
            while currNode.next and currNode.val == currNode.next.val:
                currNode = currNode.next
            #currNode now points to the last node that has its value, skipping any duplicates before it
            if prevNode.next == currNode: #If no elements were skipped (i.e. deleted)
                prevNode.next = currNode
                prevNode = currNode #Set prevNode to point to currNode and increment both pointers normally
                currNode = currNode.next
            else:
                currNode = currNode.next #Increment currNode again to push it just beyond the group of duplicates
                prevNode.next = currNode
                #Do not increment prevNode since we just performed a deletion

        return dummyNode.next




def main():
    solution = Solution()
    nums = [1,2,3,3,4,4,5]
    head1 = createList(nums)
    ans = solution.deleteDuplicates(head1) # [1,2,5]
    ans.printList()
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method