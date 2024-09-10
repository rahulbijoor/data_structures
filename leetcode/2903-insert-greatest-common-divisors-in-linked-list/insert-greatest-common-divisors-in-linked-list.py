# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, (a % b))
        while curr:
            if prev:
                g = gcd(prev.val,curr.val)
                newNode = ListNode(g)
                prev.next = newNode
                newNode.next = curr

            
            prev = curr
            curr = curr.next
        return head