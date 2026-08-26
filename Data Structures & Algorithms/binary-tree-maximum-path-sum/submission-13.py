# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def dfs(node: TreeNode):
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, node.val + left + right, node.val, node.val +left, node.val + right)
            return node.val + max(left, right, 0)
        

        dfs(root)
        return res