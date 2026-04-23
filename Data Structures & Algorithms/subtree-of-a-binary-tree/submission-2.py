# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def helper(main, sub):
            if not main and not sub:
                return True
            
            if main and sub and main.val == sub.val:
                return helper(main.left, sub.left) and helper(main.right, sub.right)

            return False
        
        if not subRoot:
            return False
        if not root:
            return False
        

        if helper(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        