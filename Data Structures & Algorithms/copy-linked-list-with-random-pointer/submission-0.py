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

        def helper(node):
            if not node:
                return None
            if node in dic:
                return dic[node]

            
            copy = Node(node.val)
            dic[node] = copy
            copy.next = helper(node.next)

            if node.random:
                copy.random = dic[node.random]
            else:
                copy.random = None

            return copy
        

        return helper(head)