"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dic = {}

        def dfs(cur, prev):
            if not cur:
                return None
            if cur in dic:
                return dic[cur]
            
            copy = Node(cur.val)
            dic[cur] = copy
            for nei in cur.neighbors:
                if nei == prev:
                    copy.neighbors.append(dic[nei])
                    continue
                
                copy.neighbors.append(dfs(nei, cur))


            return copy

        

        return dfs(node, None)