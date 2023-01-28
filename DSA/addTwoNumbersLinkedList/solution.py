from typing import Optional

#https://leetcode.com/problems/add-two-numbers

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode() #The linked list we use to store our results
        ret = ans #Save a copy of the head of our linked list, since the ans variable will be incremented
        carry = 0
        #Have to be cautious about whether l1 or l2 are valid, since one might have more digits than the other
        while l1 != None or l2 != None : #While either l1 or l2 are valid ...
            if l1 : ans.val += l1.val #Add l1 to current digit if l1 is valid
            if l2 : ans.val += l2.val #Add l2 to current digit if l1 is valid
            ans.val += carry
            carry = 0
            if ans.val >= 10 : #If current digit exceeds 9, then we have to set the carry and adjust the current digit
                ans.val = ans.val % 10
                carry = 1
            if l1 : l1 = l1.next #Only move forward if l1 is valid
            if l2 : l2 = l2.next #Only move forward if l2 is valid
            #If l1 or l2 were at their last digit, then they are now equal to 'None' after the above line
            #This allows the line below to work, since l1 or l2 now equal 'None' if we have processed all their digits
            if l1 or l2 : #Only add a new digit to our answer if there are more digits for us to process
                ans.next = ListNode()
                ans = ans.next
            
        if carry != 0 : #After the loop, we still have to handle the carry if there is any
            ans.next = ListNode(carry)

        return ret


def main():
    print('Would have to instantiate a linked list to execute it here')

if __name__ == "__main__": #Entry point
    main() #Calling main method