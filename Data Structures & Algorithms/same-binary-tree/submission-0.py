# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        one, two = p, q
        if one and two and one.val == two.val:
            return (self.isSameTree(one.left, two.left) and self.isSameTree(one.right, two.right))
        else:
            return False