# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, leftBound, rightBound):
            if not node: return True

            if not (leftBound < node.val < rightBound):
                return False
            

            return helper(node.left, leftBound, node.val) and helper(node.right, node.val, rightBound)
            


        return helper(root, float("-inf"), float("inf"))