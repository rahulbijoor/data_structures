# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = curr = ListNode()
        
        # Initialize a variable to store the remainder value, if any, as we compute the sum. 
        remainder = 0
        
        # Traverse the two lists while our two pointers is not null and remainder is not 0.
        while l1 or l2 or remainder:
            
            # Find the values at each pointer
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            
            # Find and store their sum
            total = num1 + num2 + remainder
            singleDigitTotal = total % 10
            
            # Calculate the carry over value, if any
            remainder = total // 10 
            
            # Create and attach a new node with summed value to the return list
            curr.next = ListNode(singleDigitTotal)
            
            # Repeat with next nodes
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        # Return dummy.next
        return dummyNode.next   
        