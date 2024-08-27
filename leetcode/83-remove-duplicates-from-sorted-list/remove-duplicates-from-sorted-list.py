# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes = set()
        curr = head
        prev = None
        while curr:

            if curr.val not in nodes:
                nodes.add(curr.val)
                prev = curr
            else:
                prev.next = curr.next

            curr = curr.next
        return head

        