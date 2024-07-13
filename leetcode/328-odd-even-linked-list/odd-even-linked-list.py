# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        odd=head
        evenhead=head.next
        even=head.next

        while even and even.next:
            odd.next = even.next  # Link odd-indexed nodes
            odd = odd.next
            even.next = odd.next  # Link even-indexed nodes
            even = even.next

        odd.next=evenhead

        return head 