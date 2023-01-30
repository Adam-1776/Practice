from typing import Optional

#https://leetcode.com/problems/merge-two-sorted-lists/


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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        #Think about how to structure your while loop, whether to run it while both list1 and list2 are valid,
        #or whether to run it while either is valid. In this case, it's cleaner to only run it while both are valid,
        #since we can easily just append the surviving list after the loop is complete. On the other hand,
        #using a 'or' loop made more sense in the add two numbers problem, since you can just assign 0 as the value of the dead node
        #and keep the loop going till both nodes are dead.
        while list1 and list2:
            if list1.val < list2.val :
                cur.next = ListNode(list1.val)
                list1 = list1.next #Be careful, we only advance one list in each iteration
            else :
                cur.next = ListNode(list2.val)
                list2 = list2.next
            cur = cur.next
        while list1 : 
            cur.next = ListNode(list1.val)
            cur = cur.next
            list1 = list1.next
        while list2 : 
            cur.next = ListNode(list2.val)
            cur = cur.next
            list2 = list2.next
        return dummy.next


def main():
    solution = Solution()
    nums = [1,4,6,7]
    nums2 = [2,3,5,7,8]
    head1 = createList(nums)
    head2 = createList(nums2)
    ans = solution.mergeTwoLists(head1, head2)
    ans.printList()
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method