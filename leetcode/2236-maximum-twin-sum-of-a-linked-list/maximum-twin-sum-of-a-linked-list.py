# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        result=0
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow= slow.next
        
        nextNode=slow
        prev=None
        while slow:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode
        result=0
        curr=head
        while prev:
            result=max(result,curr.val+prev.val)
            prev=prev.next
            curr=curr.next
            
        return result