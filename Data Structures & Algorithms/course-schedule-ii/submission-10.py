from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = defaultdict(list)

        for course, pre in prerequisites:
            dic[course].append(pre)

        
        res = []
        visiting = set()
        visited = set()
        def dfs(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True

            visiting.add(course)
            flag = True
            for pre in dic[course]:
                if not dfs(pre):
                    flag = False
                    break
            visiting.remove(course)
            if not flag:
                return False

            visited.add(course)
            res.append(course)
            return True
                    


        for course in range(numCourses):
            if not dfs(course):
                return []

        return res if len(res) == numCourses else []

        

        


