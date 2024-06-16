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
        
        # Step 1: Initialize a temp node to simplify edge cases
        temp = ListNode(0)
        temp.next = head
        curr = temp
        
        # Step 2: Reach the node just before position `left`
        position = 1
        while position < left:
            curr = curr.next
            position += 1
        
        # Step 3: Reverse the sublist from `left` to `right`
        sublist_head = curr.next
        prev = None
        position = left
        while position <= right:
            next_node = sublist_head.next
            sublist_head.next = prev
            prev = sublist_head
            sublist_head = next_node
            position += 1
        
        # Step 4: Connect the reversed sublist back to the main list
        curr.next.next = sublist_head
        curr.next = prev
        
        return temp.next