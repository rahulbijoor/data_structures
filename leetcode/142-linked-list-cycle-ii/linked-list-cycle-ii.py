# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #fast = head
        #slow = head
        curr = head
        nodes=dict()
        count = 0
        while curr:
            if curr in nodes.values():
                
                return curr

            nodes[count] = curr
            count += 1
            curr = curr.next
            #fast = fast.next.next
            #slow = slow.next
        
        return None