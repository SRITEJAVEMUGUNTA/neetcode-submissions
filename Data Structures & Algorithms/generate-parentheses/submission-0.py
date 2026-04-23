class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(string, openCount, closedCount):
            if openCount == n and closedCount == n:
                res.append(string)
                return
            if openCount < n:
                backtrack(string + "(", openCount + 1, closedCount)

            if closedCount < openCount:
                backtrack(string + ")", openCount, closedCount+1)


        
        backtrack("",0,0)
        return res