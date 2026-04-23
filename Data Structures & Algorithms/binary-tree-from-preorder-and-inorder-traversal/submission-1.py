# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def helper(pre, ino):
            if not pre or not ino:
                return

            
            
            rootVal = pre[0]
            root = TreeNode(rootVal)
            inorderIdx = ino.index(rootVal)

            inoLeft = ino[0:inorderIdx]
            inoRight = ino[inorderIdx+1:]


            preLeft = pre[1:len(inoLeft)+1]
            preRight = pre[len(inoLeft)+1:]

            root.left = helper(preLeft,inoLeft)
            root.right = helper(preRight,inoRight)


            return root
            


        

        return helper(preorder, inorder)