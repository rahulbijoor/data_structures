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
        
        # Step 1: Initialize a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Step 2: Reach the node just before position `left`
        position = 1
        while position < left:
            prev = prev.next
            position += 1
        
        # Step 3: Reverse the sublist from `left` to `right`
        current = prev.next
        next_node = None
        sublist_head = current
        
        position = left
        while position <= right:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            position += 1
        
        # Step 4: Connect the reversed sublist back to the main list
        sublist_head.next = current
        prev_before_sublist = dummy
        while prev_before_sublist.next != sublist_head:
            prev_before_sublist = prev_before_sublist.next
        prev_before_sublist.next = prev
        
        return dummy.next