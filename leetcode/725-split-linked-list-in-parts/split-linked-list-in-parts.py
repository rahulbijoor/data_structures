# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        mod = count%k
        minNum = count//k
        print(minNum)
        result = []
        curr = head
        for j in range(k):
            part_Head = curr
            part_Size = minNum + (1 if j < mod else 0)
            prev = None
            for _ in range(part_Size):
                prev = curr
                if curr:
                    curr = curr.next
            if prev:
                prev.next = None
            result.append(part_Head)
        return result

        
        
        return result