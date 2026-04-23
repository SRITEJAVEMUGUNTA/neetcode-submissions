# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        

        def helper(node, curMax):
            if not node:
                return
            
            if node.val >= curMax:
                print(node.val)
                res[0] += 1
                helper(node.left,node.val)
                helper(node.right,node.val)
            else:
                helper(node.left,curMax)
                helper(node.right,curMax)

        
        helper(root, float("-inf"))


        return res[0]