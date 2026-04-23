from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)

        visited = set()
        visiting = set()

        for course, pre in prerequisites:
            dic[course].append(pre)

        def dfs(course):
            if course in visited:
                return True
            
            if course in visiting:
                return False
            


            flag = True
            visiting.add(course)
            for pre in dic[course]:
                if not dfs(pre):
                    flag = False
                    break
            visiting.remove(course)

            if flag:
                visited.add(course)
                return True
            return False

        for num in range(numCourses):
            if not dfs(num):
                return False
        
        return True


        

        