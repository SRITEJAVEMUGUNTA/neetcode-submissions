# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l, r = head, head.next

        while(r and r.next):
            l = l.next
            r = r.next.next
        
        middle = l.next
        l.next = None
        prev = None
        while middle:
            temp = middle.next
            middle.next = prev
            prev = middle
            middle = temp
        
        x, y = head, prev

        while y:
            temp1, temp2 = x.next, y.next
            x.next = y
            y.next = temp1
            y = temp2
            x = temp1
        


