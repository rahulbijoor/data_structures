# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)  # Dummy node to simplify code
        current = dummy
        carry = 0
        
        while l1 is not None or l2 is not None:
            sum = carry
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            
            carry = sum // 10  # Integer division for carry
            current.next = ListNode(sum % 10)  # Modulus for the current digit
            current = current.next
        
        if carry > 0:
            current.next = ListNode(carry)
        
        return dummy.next