# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            nextVal = l1.val + l2.val + carry

            if nextVal >= 10:
                carry = 1
                nextVal -= 10
            else:
                carry = 0
            
            nodeToAdd = ListNode(nextVal)
            cur.next = nodeToAdd
            cur = nodeToAdd
            l1 = l1.next
            l2 = l2.next

        while l1:
            print("Hello")
            nextVal = l1.val + carry
            print(nextVal)
            if nextVal >= 10:
                carry = 1
                nextVal -= 10
            else:
                carry = 0
            nodeToAdd = ListNode(nextVal)
            cur.next = nodeToAdd
            cur = nodeToAdd
            l1 = l1.next
        while l2:
            nextVal = l2.val + carry
            if nextVal >= 10:
                carry = 1
                nextVal -= 10
            else:
                carry = 0
            nodeToAdd = ListNode(nextVal)
            cur.next = nodeToAdd
            cur = nodeToAdd
            l2 = l2.next

        
        if carry == 1:
            cur.next = ListNode(1)
            
        

        return dummy.next