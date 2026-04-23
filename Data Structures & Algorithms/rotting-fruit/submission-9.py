from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rowLen = len(grid)
        colLen = len(grid[0])
        q = deque()
        freshFruit = [0]
        def checkFruitAddition(r,c):
            if r < 0 or r >= rowLen or c < 0 or c >= colLen:
                return
            
            if grid[r][c] != 1:
                return
            
            freshFruit[0] -= 1
            grid[r][c] = 2
            q.append((r,c))

        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    freshFruit[0] += 1

        if not freshFruit[0]:
            return 0
            
        if not q:
            return -1

        

        time = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()

                checkFruitAddition(r+1,c)
                checkFruitAddition(r,c+1)
                checkFruitAddition(r-1,c)
                checkFruitAddition(r,c-1)

            time += 1
        
        return time - 1 if freshFruit[0] == 0 else -1


                
