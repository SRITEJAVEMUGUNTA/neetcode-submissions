class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        visited_pac = set()
        visited_atl = set()
        cols = len(heights[0])
        rows = len(heights)
        
        
        def dfs(r,c, visited):
            visited.add((r,c))


            directions = [(-1,0), (1,0), (0, -1), (0, 1)]

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if(row in range(rows) and col in range(cols) and
                heights[row][col] >= heights[r][c] and
                (row, col) not in visited):
                    dfs(row, col, visited)



        for x in range(rows):
            dfs(x, cols - 1, visited_atl)
            dfs(x, 0, visited_pac)
        for x in range(cols):
            dfs(0, x, visited_pac)
            dfs(rows - 1, x, visited_atl)

        return list(visited_pac & visited_atl)