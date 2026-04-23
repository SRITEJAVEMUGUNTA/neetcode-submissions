# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        

        idxInorder = inorder.index(preorder[0])

        leftIn = inorder[:idxInorder]
        rightIn = inorder[idxInorder+1:]

        leftPre = preorder[1:len(leftIn)+1]
        rightPre = preorder[len(leftIn)+1:]

        rootVal = preorder[0]
        root = TreeNode(rootVal)

        root.left = self.buildTree(leftPre, leftIn)
        root.right = self.buildTree(rightPre, rightIn)

        return root