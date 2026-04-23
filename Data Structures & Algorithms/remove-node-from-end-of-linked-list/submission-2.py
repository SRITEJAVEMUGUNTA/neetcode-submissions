# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        dummy = ListNode(0, head)
        prev = dummy
        p = head

        for _ in range(n):
            p = p.next
        
        while p:
            prev = prev.next
            p = p.next

        prev.next = prev.next.next

        return dummy.next
        