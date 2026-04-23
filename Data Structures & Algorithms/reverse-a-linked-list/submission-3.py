# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, rev = None, head

        while rev:
            temp = rev.next
            rev.next = prev
            prev = rev
            rev = temp
        return prev
