from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()
        rowLen = len(grid)
        colLen = len(grid[0])

        def helper(r,c):
            if r < 0 or r >= rowLen or c < 0 or c >= colLen:
                return
            
            if grid[r][c] == -1 or (r,c) in visited:
                return
            
            visited.add((r,c))
            q.append([r,c])

        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append([r,c])
        
        distance = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = distance

                helper(r+1,c)
                helper(r-1,c)
                helper(r,c+1)
                helper(r,c-1)

            distance += 1


