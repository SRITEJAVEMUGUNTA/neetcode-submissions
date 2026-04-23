class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])

        def dfs(r,c):
            if r < 0 or r >= rowLen or c < 0 or c >= colLen:
                return 0
            
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0


            val = dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

            return 1 + val

        


        res = 0
        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 1:
                    res = max(res, dfs(r,c))

        return res

        