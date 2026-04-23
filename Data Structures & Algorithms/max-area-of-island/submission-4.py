class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        res = [0]
        visited = set()
        def dfs(r,c):
            if r < 0 or r >= rowLen or c < 0 or c >= colLen:
                return 0

            if grid[r][c] == 0:
                return 0
            
            if (r,c) in visited:
                return 0
            
            visited.add((r,c))

            curSol = 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
            
            res[0] = max(res[0], curSol)

            return curSol


        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 1 and (r,c) not in visited:
                    dfs(r,c)
        

        return res[0]

        