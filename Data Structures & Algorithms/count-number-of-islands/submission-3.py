class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rowLen = len(grid)
        colLen = len(grid[0])

        def dfs(r,c):
            if r < 0 or r >= rowLen or c < 0 or c >= colLen:
                return

            if (r,c) in visited or grid[r][c] == "0":
                return

            visited.add((r,c))

            

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        
        res = 0

        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    res += 1

        return res