class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        boxSet = defaultdict(set)
        

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue

                num = board[r][c]

                if num in rowSet[r]:
                    return False
                rowSet[r].add(num)

                if num in colSet[c]:
                    return False
                colSet[c].add(num)

                tup = (r//3, c//3)

                if num in boxSet[tup]:
                    return False
                boxSet[tup].add(num)

        return True
