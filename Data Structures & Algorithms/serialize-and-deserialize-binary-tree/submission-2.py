# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    #PreOrder Traversal
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        arr = data.split(",")

        idx = [0]

        def preOrder():
            if arr[idx[0]] == "N":
                return None
            
            node = TreeNode(int(arr[idx[0]]))
            idx[0] += 1
            node.left = preOrder()
            idx[0] += 1
            node.right = preOrder()


            return node
        

        return preOrder()

        