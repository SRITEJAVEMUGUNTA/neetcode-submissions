class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        delimeter = 2147483647
        rowLen = len(grid)
        colLen = len(grid[0])
        q = deque()
        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 0:
                    q.append((r,c))
        distance = 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        while q:
            distance += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                for dx,dy in directions:
                    if dx + r < 0 or dx + r >= rowLen: continue
                    if dy + c < 0 or dy + c >= colLen: continue
                    x = dx+r
                    y = dy+c
                    if grid[x][y] != delimeter: continue
                    grid[x][y] = distance
                    q.append((x,y))

    
                