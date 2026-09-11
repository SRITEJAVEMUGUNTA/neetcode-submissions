# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [1]
        res = None
        def dfs(node):
            nonlocal res
            if not node: return
            dfs(node.left)
            if count[0] == k and not res:
                res = node
            count[0] += 1
            dfs(node.right)

        dfs(root)
        return res.val