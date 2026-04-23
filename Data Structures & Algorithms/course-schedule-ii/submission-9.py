from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = defaultdict(list)

        for course, pre in prerequisites:
            dic[course].append(pre)

        res = []
        visited = set()
        visiting = set()
        def dfs(course):
            if course in visited:
                return True
            
            if course in visiting:
                return False

            visiting.add(course)
            flag = True
            for pre in dic[course]:
                if not dfs(pre):
                    flag = False
                    break
                
      
            if not flag:
                return False

            res.append(course)
            visited.add(course)
            return True



        for num in range(numCourses):
            dfs(num)

        return res if len(res) == numCourses else []