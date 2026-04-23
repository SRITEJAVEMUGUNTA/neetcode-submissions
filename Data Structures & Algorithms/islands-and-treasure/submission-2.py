from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rowLen = len(grid)
        colLen = len(grid[0])
        q = deque()

        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 0:
                    q.append((r,c))

        val = 2147483647

        distanceFromChest = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if nr < 0 or nr >= rowLen or nc < 0 or nc >= colLen:
                        continue
                    
                    if grid[nr][nc] != val:
                        continue
                    
                    grid[nr][nc] = distanceFromChest + 1

                    q.append((nr,nc))

            distanceFromChest += 1
                    




        



