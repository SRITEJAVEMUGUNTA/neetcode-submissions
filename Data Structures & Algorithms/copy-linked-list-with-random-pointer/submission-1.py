"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = {}

        def copyHelper(node):
            if not node: return None

            copy = Node(node.val)
            dic[node] = copy
            copy.next = copyHelper(node.next)
            
            if node.random:
                copy.random = dic[node.random]

            return copy



        return copyHelper(head)