# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
    
        sum_value = 0
        slow = dummy
        curr = head
    
        while curr is not None:
            if curr.val == 0:
                if sum_value != 0:
                    new_node = ListNode(sum_value)
                    slow.next = new_node
                    slow = slow.next
                    sum_value = 0
            else:
                sum_value += curr.val
        
            curr = curr.next
    
    # Handle the last accumulated sum
        if sum_value != 0:
            new_node = ListNode(sum_value)
            slow.next = new_node
    
        return dummy.next

