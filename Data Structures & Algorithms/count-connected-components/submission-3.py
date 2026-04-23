from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dic = defaultdict(list)
        if not edges:
            return n
        for start, end in edges:
            dic[start].append(end)
            dic[end].append(start)
        count = 0
        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for nei in dic[node]:
                dfs(nei)
            

        
        

        for start in range(0,n):
            if start not in visited:
                count += 1
                dfs(start)

        return count
                

