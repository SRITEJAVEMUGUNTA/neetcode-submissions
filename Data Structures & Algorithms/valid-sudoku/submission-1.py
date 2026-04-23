class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horiz = defaultdict(set)

        vert = defaultdict(set)

        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if(board[r][c] == "."):
                    continue
                if(board[r][c] in horiz[r] or board[r][c]  in vert[c] or board[r][c] in box[(r//3, c//3)]):
                    return False
                
                horiz[r].add(board[r][c])
                vert[c].add(board[r][c])
                box[(r//3, c//3)].add(board[r][c])
        return True
                
                