# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]

        def helper(big, node):
            if not node:
                return
            
            if node.val >= big:
                res[0] += 1

            newBig = max(big, node.val)
            
            helper(newBig, node.left)
            helper(newBig, node.right)
        helper(float("-inf"), root)
        return res[0]