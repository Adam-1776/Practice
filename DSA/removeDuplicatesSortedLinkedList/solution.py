from typing import Optional

#https://leetcode.com/problems/remove-duplicates-from-sorted-list/


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
    #Two pointers approach
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        curNode = head.next #Right pointer
        leftNode = head #Left pointer
        while curNode != None:
            if curNode.val != leftNode.val: #If left pointer and right pointer do not match, make the left node point to the right
                leftNode.next = curNode
                leftNode = curNode #Only move the left pointer if we have made a connection between two unique successive nodes.
                curNode = curNode.next
            else:
                curNode = curNode.next #If the left and right pointers point to nodes with the same value, only increment the right pointer
        leftNode.next = None #After the loop, the left pointer points to the last unique node. End the list here.
        return head

    #Alternate approach using single pointer
    def deleteDuplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        current = head
        while current.next: #Keep going until the second last Node since we compare the current node with the one ahead of it
            if current.val == current.next.val: #If the next node has the same value
                current.next = current.next.next #Make the current node point to the one twice ahead
            else: #Use an else statement since we don't want to increment the current node if we just skipped a duplicate (common pattern to not increment prev pointer when doing deletion in a linked list)
                current = current.next #Once we find a unique node in front of current, move the current node to it. This will skip any duplicate nodes we had encountered
        return head


def main():
    solution = Solution()
    nums = [1,2,2,3,3,3,3,4,4,5,6,7,7]
    head1 = createList(nums)
    ans = solution.deleteDuplicates(head1)
    ans.printList()
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method