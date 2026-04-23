'''
fill the two sets with the intial elements of both
then iterate over one set and and see how much it can cover
do the same with the other

(use q for iteration)
return the union of both sets
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        atlQ = deque()
        pacQ = deque()
        rowLen = len(heights)
        colLen = len(heights[0])
        pac = [[False] * colLen for _ in range(rowLen)]
        atl = [[False] * colLen for _ in range(rowLen)]
        directions = [[1,0],[-1,0], [0,1], [0,-1]]
        def bfs(q, ocean):

            while q:
                r,c = q.popleft()
                ocean[r][c] = True

                for dx, dy in directions:
                    nr, nc = r + dx, c + dy

                    if nr < 0 or nr >= rowLen or nc < 0 or nc >= colLen:
                        continue

                    if not ocean[nr][nc] and heights[nr][nc] >= heights[r][c]:
                        q.append([nr,nc])


        for r in range(rowLen):
            for c in range(colLen):
                if r == 0 or c == 0:
                    pacQ.append([r,c])
                if r == rowLen-1 or c == colLen-1:
                    atlQ.append([r,c])

        bfs(atlQ, atl)
        bfs(pacQ, pac)
        res = []
        for r in range(rowLen):
            for c in range(colLen):
                if atl[r][c] and pac[r][c]:
                    res.append([r,c])

        return res

        

        


