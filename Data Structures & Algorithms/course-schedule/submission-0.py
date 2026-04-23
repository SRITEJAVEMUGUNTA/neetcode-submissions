class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)

        for crs, pre in prerequisites:
            dic[crs].append(pre)
        
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if dic[crs] == []:
                return True
            
            visited.add(crs)
            for pre in dic[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            dic[crs] = []
            return True
        

        for x in range(numCourses):
            if not dfs(x):
                return False
        return True