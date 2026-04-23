from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dic = defaultdict(list)

        for one, two in edges:
            dic[one].append(two)
            dic[two].append(one)


        seen = set()

        def dfs(node, pre):
            if node in seen:
                return False
            
            seen.add(node)

            for nei in dic[node]:
                if nei == pre:
                    continue
                if not dfs(nei, node):
                    return False

            return True
        


        

        return dfs(0, -1) and len(seen) == n


