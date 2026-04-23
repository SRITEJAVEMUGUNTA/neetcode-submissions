class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dic = defaultdict(list)
        for x, y in edges:
            dic[x].append(y)
            dic[y].append(x)
        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)
            for num in dic[i]:
                if num == prev:
                    continue
                
                if not dfs(num, i):
                    return False
            
            return True
                
        return dfs(0, -1) and n == len(visited)