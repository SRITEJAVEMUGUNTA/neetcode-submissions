# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = [None]
        def helper(node):
            if not node:
                return 0
            total = 0
            if node == p:
                total += 1
            elif node == q:
                total += 1
            
            sumTotal = total + helper(node.left) + helper(node.right)
            if sumTotal >= 2 and res[0] == None:
                res[0] = node
            
            return sumTotal
        
        helper(root)
        return res[0]
        
