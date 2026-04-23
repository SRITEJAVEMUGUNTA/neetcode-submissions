class Solution:
    def solve(self, board: List[List[str]]) -> None:

        q = deque()
        rowLen = len(board)
        colLen = len(board[0])
        insideCircles = 0

        def checkForCircles(r,c):
            nonlocal insideCircles
            if r < 0 or r >= rowLen or c < 0 or c >= colLen:
                return
            
            if board[r][c] != "O":
                return
            

            board[r][c] = "*"
            insideCircles -= 1
            q.append((r,c))


        for r in range(rowLen):
            for c in range(colLen):
                if board[r][c] == "O":
                    if r == 0 or r == rowLen - 1 or c == 0 or c == colLen -1:
                        q.append((r,c))
                        board[r][c] = "*"

                    else:
                        insideCircles += 1

        
        while insideCircles and q:
            
            r,c = q.popleft()

            checkForCircles(r+1,c)
            checkForCircles(r-1,c)
            checkForCircles(r,c+1)
            checkForCircles(r,c-1)

        for r in range(rowLen):
            for c in range(colLen):
                if board[r][c] == "*":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"



