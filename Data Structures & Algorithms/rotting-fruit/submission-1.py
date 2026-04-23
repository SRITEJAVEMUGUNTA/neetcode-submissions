class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0
        rowLen = len(grid)
        colLen = len(grid[0])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q and fresh > 0:

            for _ in range(len(q)):
                r,c = q.popleft()

                for addR, addC in directions:
                    nR, nC = r + addR, c+addC

                    if 0 <= nR < rowLen and 0 <= nC < colLen and grid[nR][nC] == 1:
                        grid[nR][nC] = 2
                        fresh -= 1
                        q.append((nR,nC))

            time += 1

        return time if fresh == 0 else -1