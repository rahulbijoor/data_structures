# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast=head
        slow=head
        if not head.next.next:
            return head.next.val+head.val

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid=slow
        prev = None
        front = None
        curr=slow

        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front

        begin = head
        secondhalf = prev
        maxValue=0
        while secondhalf:
            maxValue = max(maxValue, begin.val+secondhalf.val)
            secondhalf=secondhalf.next
            begin=begin.next
        
        return maxValue
