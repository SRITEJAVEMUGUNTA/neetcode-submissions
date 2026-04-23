from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dic = defaultdict(list)

        for cur, nei in edges:
            dic[cur].append(nei)
            dic[nei].append(cur)
        
        visiting = set()
        visited = set()
        def dfs(prev, num):
            if num in visiting:
                return False

            if num in visited:
                return True

            visiting.add(num)


            for nei in dic[num]:
                if nei == prev:
                    continue
                if not dfs(num, nei):
                    return False
            
            visiting.remove(num)
            visited.add(num)
            return True

        dfs(None, 0)
        return True if len(visited) == n else False
        
        




