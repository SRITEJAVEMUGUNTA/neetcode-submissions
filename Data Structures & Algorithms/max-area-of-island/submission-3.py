class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visited = set()
        count = [0]
        rows, cols = len(grid), len(grid[0])

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            cur = 1

            while q:
                row, col = q.popleft()
                directions = [(-1,0), (1,0), (0, -1), (0, 1)]

                for dx, dy in directions:
                    r, c = row + dx, col + dy

                    if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] == 1:
                        visited.add((r,c))
                        q.append((r,c))
                        cur += 1
            count[0] = max(count[0], cur)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    bfs(r,c)
        
        return count[0]
