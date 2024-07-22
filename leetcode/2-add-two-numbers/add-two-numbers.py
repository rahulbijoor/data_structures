# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3=ListNode(0)
        dummy=l3
        carry = 0
        while l1 and l2 :
            addSum = l1.val + l2.val + carry
            carry = addSum // 10
            l3.next=ListNode(addSum % 10)
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            addSum = l1.val + carry 
            carry = addSum // 10
            l3.next=ListNode(addSum % 10)
            l3 = l3.next
            l1 = l1.next
        while l2:
            addSum = l2.val + carry
            carry = addSum // 10
            l3.next=ListNode(addSum % 10)
            l3 = l3.next
            l2 = l2.next
        

        
        if carry == 1:
            l3.next=ListNode(carry)
        
        return dummy.next

