class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])

        def dfs(r,c):
            if r < 0 or r >= rowLen or c < 0 or c >= colLen:
                return

            if grid[r][c] == "0":
                return

            grid[r][c] = "0"

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        
        res = 0

        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == "1":
                    dfs(r,c)
                    res += 1

        return res