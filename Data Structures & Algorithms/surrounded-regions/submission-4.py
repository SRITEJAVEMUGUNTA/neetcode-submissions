class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rowLen = len(board)
        colLen = len(board[0])
        q = deque()
        for r in range(rowLen):
            if board[r][0] == "O":
                q.append((r,0))
                board[r][0] = "S"
            if board[r][colLen - 1] == "O":
                q.append((r, colLen-1))
                board[r][colLen - 1] = "S"
        for c in range(colLen):
            if board[0][c] == "O":
                q.append((0,c))
                board[0][c] = "S"
            if board[rowLen - 1][c] == "O":
                q.append((rowLen-1, c))
                board[rowLen-1][c] = "S"

        directions = [(-1,0), (0,-1), (0,1), (1,0)]
        while q:
            r, c = q.popleft()
            for rx, cx in directions:
                if r + rx < 0 or r + rx >= rowLen:
                    continue
                if c + cx < 0 or c + cx >= colLen:
                    continue
                if board[r+rx][c+cx] == "O":
                    board[r+rx][c+cx]= "S"
                    q.append((r+rx, c+cx))

        for r in range(rowLen):
            for c in range(colLen):
                if board[r][c] == "S":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
            
            
            


