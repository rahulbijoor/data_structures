# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nodes=[]
        curr=head
        while curr:
            nodes.append(curr.val)
            curr=curr.next
        result=0
        for i in range(len(nodes)//2):
            result=max(result,nodes[i]+nodes[len(nodes)-1-i])
        
        return result