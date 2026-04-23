
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowLen = len(board)
        colLen = len(board[0])
        def helper(r,c, idx, seen):
            if idx >= len(word):
                return True
            if (r < 0 or r >= rowLen or c < 0 or c >= colLen):
                return False
            
            if board[r][c] != word[idx]:
                return False
            print(board[r][c])
            print(r)
            print(c)
            print('\n')
            if (r,c) in seen:
                return False
            seen.add((r,c))

            res = (helper(r+1,c,idx+1,seen) or
                    helper(r-1,c,idx+1,seen) or 
                    helper(r,c+1,idx+1,seen) or
                    helper(r,c-1,idx+1,seen))

            seen.remove((r,c))
            return res

        for r in range(rowLen):
            for c in range(colLen):
                if board[r][c] == word[0] and helper(r,c,0, set()):
                    return True
        
        return False
                