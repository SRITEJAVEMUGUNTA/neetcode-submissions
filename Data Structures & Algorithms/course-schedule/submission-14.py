class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        dic = defaultdict(list)

        for course, pre in prerequisites:
            dic[course].append(pre)

        visiting = set()
        visited = set()
        
        def dfs(course):
            if course in visited:
                return True

            if course in visiting:
                return False

            

            

            visiting.add(course)

            
            
            flag = True
            for req in dic[course]:
                if not dfs(req):
                    flag = False
                    break

            print(course)
            

            if not flag:
                return False
            
            visited.add(course)
            return True


        for course in range(numCourses):
            if not dfs(course):

                return False

        return True
