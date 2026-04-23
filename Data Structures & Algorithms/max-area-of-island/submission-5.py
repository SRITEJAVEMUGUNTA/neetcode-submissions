class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = [0]
        rowLen = len(grid)
        colLen = len(grid[0])
        def dfs(r,c):
            if r < 0 or r >= rowLen or c < 0 or c>= colLen:
                return 0
            
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 1:
                    res[0] = max(res[0], dfs(r,c))

        return res[0]
        



