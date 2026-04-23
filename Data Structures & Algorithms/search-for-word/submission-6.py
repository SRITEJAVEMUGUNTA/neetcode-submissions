class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowLen, colLen = len(board), len(board[0])
        seen = set()   # global visited set

        def helper(r, c, idx):
            if idx >= len(word):
                return True
            if r < 0 or r >= rowLen or c < 0 or c >= colLen:
                return False
            if board[r][c] != word[idx]:
                return False
            if (r, c) in seen:
                return False

            seen.add((r, c))
            res = (helper(r+1, c, idx+1) or
                   helper(r-1, c, idx+1) or
                   helper(r, c+1, idx+1) or
                   helper(r, c-1, idx+1))
            seen.remove((r, c))
            return res

        for r in range(rowLen):
            for c in range(colLen):
                if board[r][c] == word[0]: # reset between different starting points
                    if helper(r, c, 0):
                        return True

        return False
