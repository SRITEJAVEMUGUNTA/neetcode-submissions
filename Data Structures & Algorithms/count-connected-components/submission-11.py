from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dic = defaultdict(list)


        for nodeOne, nodeTwo in edges:
            dic[nodeOne].append(nodeTwo)
            dic[nodeTwo].append(nodeOne)

        visited = set()
        visiting = set()

        def dfs(prev, node):
            if node in visiting:
                return

            visiting.add(node)

            for nei in dic[node]:
                if nei not in visited:
                    dfs(node, nei)

            visiting.remove(node)
            
            visited.add(node)

        res = 0
        for num in range(n):
            if num not in visited:
                res += 1
                dfs(None,num)
            
            if len(visited) == n:
                return res

        return res
                

        
