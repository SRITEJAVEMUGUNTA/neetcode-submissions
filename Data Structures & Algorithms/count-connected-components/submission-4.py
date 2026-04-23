from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dic = defaultdict(list)
        for one, two in edges:
            dic[one].append(two)
            dic[two].append(one)

        seen = set()
        def dfs(node, prev):
            if node in seen:
                return
            
            seen.add(node)

            for nei in dic[node]:
                dfs(nei, node)

        res = 0
        for num in range(n):
            if num not in seen:
                dfs(num, -1)
                res += 1
        

        return res