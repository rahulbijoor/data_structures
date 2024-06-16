# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or left == right:
            return head
        
        # Step 1: Reach the node at position `left`
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for _ in range(left - 1):
            prev = prev.next
        
        # Step 2: Reverse the sublist
        current = prev.next
        next_node = None
        prev_sublist = prev
        
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Step 3: Connect the reversed sublist back to the main list
        prev_sublist.next.next = current
        prev_sublist.next = prev
        
        return dummy.next