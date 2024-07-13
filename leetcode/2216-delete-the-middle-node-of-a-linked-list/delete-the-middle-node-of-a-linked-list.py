# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        prev=ListNode(0)
        slow=head
        fast=head

        while fast and fast.next:
            fast=fast.next.next
            prev=slow
            slow=slow.next
        
        prev.next=slow.next
        return head
        