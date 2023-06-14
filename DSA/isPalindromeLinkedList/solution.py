from typing import Optional

#https://leetcode.com/problems/palindrome-linked-list/


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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        List = []
        while head :
            List.append(head.val)
            head = head.next
        l,r = 0,len(List)-1
        while l < r :
            if List[l] != List[r] : return False
            l += 1
            r -= 1
        return True




    #Clever approach with O(1) space complexity. Note that this is destructive to the linked list that was passed
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        fastNode = head #Use this to skip to the end of the list, not used for anything else
        slowNode = head #This is the actual 'current node'. Start it at head
        prevNode = None #This is the node behind the slowNode. Start it at None since there's nothing behind the head
        while fastNode and fastNode.next:
            fastNode = fastNode.next.next
            temp = prevNode
            prevNode = slowNode #prevNode is now slowNode, since slowNode will move forward...
            slowNode = slowNode.next #Increment slowNode
            prevNode.next = temp #Make prevNode point to the node behind it
            #Note that the ordering of the above pointer assignments is important. You can avoid this trouble of ordering by doing everything in one line,
            #such as prevNode, prevNode.next, slowNode = slowNode, prevNode, slowNode.next
            
        #At the end of the above while loop, fastNode is either the last node in the list (if there are an odd number of elements)
        #or, fastNode equals null if there are an even number of elements. This is because fastNode starts at node 1 (head) and keeps
        #jumping two steps. So it will go from node 1 to 3 to 5...
        #Meanwhile slowNode will either the exact middle if there an odd number of elements, or slowNode will be a bit right of the middle
        #if there are an even number of elements.
        #Also, since we were reversing the first half of the list in the loop above, prevNode is now a 'head' of the first half of the reversed
        #linked list. Iterating from the prevNode onwards will actually be moving from the middle of the list leftwards.
        #So basically, prevNode is now the 'head' of the first half of the reversed linked list right to left, and slowNode is the 'head' of the
        #second half of the linked list left to right

        if fastNode: #If there are an odd number of elements in the linked list...
            slowNode = slowNode.next #slowNode was at the exact middle of the list. Increment it since the exact middle isn't relevant to palindromes
        
        while prevNode and slowNode:
            if prevNode.val != slowNode.val:
                return False
            prevNode = prevNode.next
            slowNode = slowNode.next

        return True


def main():
    print('No test case')
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method