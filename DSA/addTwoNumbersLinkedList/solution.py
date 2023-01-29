from typing import Optional

#https://leetcode.com/problems/add-two-numbers


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
            if l1 : l1 = l1.next #Only move forward if l1 is valid. Need to check this in case l1 is finished and we're only processing l2
            if l2 : l2 = l2.next #Only move forward if l2 is valid. Need to check this in case l2 is finished and we're only processing l1
            #If l1 or l2 were at their last digit, then they are now equal to 'None' after the above line
            #This allows the line below to work, since l1 or l2 now equal 'None' if we have processed all their digits
            if l1 or l2 : #Only add a new digit to our answer if there are more digits for us to process
                ans.next = ListNode()
                ans = ans.next
            
        if carry != 0 : #After the loop, we still have to handle the carry if there is any
            ans.next = ListNode(carry)

        return ret

    #Same approach, but a bit more concise and elegant
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #Dummy points to an empty node before the first actual node. 
        cur = dummy #Start off with the dummy node. We haven't created any 'real' nodes yet
        carry = 0

        #Using a dummy node to start with allows us to eliminate the need to check if we need to create a new node or not for the next digit
        #Instead, we append a new node after we've computed a value for it. We don't have to create a new node in advance.
        while l1 or l2 or carry != 0:  # we will continue till either one of these have positive values left. 
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Addition: New digits
            val = v1 + v2 + carry
            carry = val // 10 #Carry will be 0 if our value is below 10
            val = val % 10 #Value will remain the same if below 10
            cur.next = ListNode(val) #Since we've computed a digit, now we create a new ListNode and append it.

            cur = cur.next #Move onto the new node that we just created in the line above
            l1 = l1.next if l1 else None #Only move l1 and l2 if we haven't reached their end yet
            l2 = l2.next if l2 else None

        #Since we included the carry in the while condition, we don't have to post-processing to ensure the final digit will be added.
        #Since the dummy node lies before the actual list begins, returning dummy.next will return the true head of the linked list.
        return dummy.next


def main():
    solution = Solution()
    nums = [4,3,2,1] #1234 since the digits are stored in reverse order
    nums2 = [8,7] #78 since the digits are stored in reverse order
    head1 = createList(nums)
    head2 = createList(nums2)
    ans = solution.addTwoNumbers2(head1, head2) #2131 which represents 1312
    ans.printList()
    
    

if __name__ == "__main__": #Entry point
    main() #Calling main method