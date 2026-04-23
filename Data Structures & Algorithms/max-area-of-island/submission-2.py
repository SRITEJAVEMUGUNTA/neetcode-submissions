class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        max_islands = [0]
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            visited.add((r,c))
            q = deque()
            q.append((r,c))
            cur_islands = 1
            while q:
            
                row, col = q.popleft()

                directions = [(-1,0), (1, 0), (0,-1), (0,1)]

                for dr, dc in directions:
                    ro = row + dr
                    co = col + dc

                    if(ro in range(rows) and co in range(cols) and grid[ro][co] == 1 and (ro,co) not in visited):
                        visited.add((ro,co))
                        q.append((ro,co))
                        cur_islands += 1
                    
            max_islands[0] = max(max_islands[0], cur_islands)

        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == 1 and (r,c) not in visited):
                    bfs(r, c)
        
        return max_islands[0]
                    