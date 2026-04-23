# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head

        slow, fast= head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
            

        # Reverse second half

        prev = None
        now = slow
        
        while now:
            nxt = now.next
            now.next = prev
            prev = now
            now = nxt

        secondCur = prev

        while (cur and secondCur):
            nxt = cur.next
            secondNxt = secondCur.next
            cur.next = secondCur
            secondCur.next = nxt
            secondCur = secondNxt
            cur = nxt
        
        
            
