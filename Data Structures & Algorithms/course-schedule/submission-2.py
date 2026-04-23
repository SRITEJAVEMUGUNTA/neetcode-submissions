from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)

        for course,pre in prerequisites:
            dic[course].append(pre)


        visited = set()
        visiting = set()
        def dfs(cur):
            if cur in visiting:
                return False
            if cur in visited:
                return True
            
            visiting.add(cur)

            flag = True
            for pre in dic[cur]:
                if not dfs(pre):
                    flag = False
            visiting.remove(cur)

            if not flag:
                return False
            
            visited.add(cur)
            return True            
        

        for num in range(numCourses):
            if not dfs(num):
                return False

        return True