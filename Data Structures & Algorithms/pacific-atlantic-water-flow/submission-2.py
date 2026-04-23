class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rowLen = len(heights)
        colLen = len(heights[0])
        def checkOcean(prevVal, r,c, oceanSet):
            if r < 0 or r >= rowLen or c < 0 or c >= colLen:
                return

            if (r,c) in oceanSet:
                return

            if heights[r][c] < prevVal:
                return
            
            oceanSet.add((r,c))

            checkOcean(heights[r][c],r+1,c,oceanSet)
            checkOcean(heights[r][c],r-1,c,oceanSet)
            checkOcean(heights[r][c],r,c-1,oceanSet)
            checkOcean(heights[r][c],r,c+1,oceanSet)


            

        aSet = set()
        pSet= set()
        for r in range(rowLen):
            for c in range(colLen):
                if r == 0 or c == 0:
                    checkOcean(-1, r,c,pSet)
                
                if r == rowLen - 1 or c == colLen -1:
                    checkOcean(-1, r,c,aSet)
        
        res = []
        for r, c in pSet:

            if (r,c) in aSet:
                res.append([r,c])

        return res