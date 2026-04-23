from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        dic = defaultdict(list)

        for course, pre in prerequisites:
            dic[course].append(pre)

        
        visited = set()
        def dfs(num, visiting):
            if num in visiting:
                return False

            if num in visited:
                return True
            
            visiting.add(num)
            flag = True
            for pre in dic[num]:
                if not dfs(pre, visiting):
                    flag = False
            visiting.remove(num)
            if not flag:
                return False
            
            res.append(num)
            visited.add(num)
            return True
        

        for num in range(numCourses):
            dfs(num, set())
            if len(res) == numCourses:
                return res

        return []
