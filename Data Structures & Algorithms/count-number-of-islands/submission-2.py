class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        res = 0
        visited = set()

        def dfs(r,c):
            if r < 0 or r >= rowLen or c < 0 or c >= colLen:
                return
            if grid[r][c] == "0":
                return

            if (r,c) in visited:
                return
            
            visited.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)


        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    res += 1
        
        return res