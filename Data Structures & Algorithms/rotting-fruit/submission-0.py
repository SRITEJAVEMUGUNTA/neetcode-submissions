from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])

        q = deque()
        freshFruit = 0
        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 2:
                    q.append((r,c))

                if grid[r][c] == 1:
                    freshFruit += 1

        count = 0
        sec = 0
        seen = set()
        while q:
            changed = False
            for _ in range(len(q)):
                r, c = q.popleft()

                if not (0 <= r < rowLen and 0 <= c < colLen):
                    continue
                if grid[r][c] == 0:
                    continue

                if (r,c) in seen:
                    continue
                
                seen.add((r,c))
                if grid[r][c] == 1:
                    changed = True
                    grid[r][c] = 2
                    count += 1
                
                q.append((r+1,c))
                q.append((r-1,c))
                q.append((r,c+1))
                q.append((r,c-1))

            if changed:
                sec += 1

        return sec if count == freshFruit else -1