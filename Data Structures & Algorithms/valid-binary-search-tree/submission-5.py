# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def helper(small, large, node):
            if not node:
                return True

            if not (small < node.val < large):
                return False
            
            return helper(node.val, large, node.right) and helper(small, node.val, node.left)
            

        return helper(float("-inf"), float("inf"), root)