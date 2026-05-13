class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return True
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        boxSet = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if(board[r][c]) == ".": continue
                num = board[r][c]
                if num in rowSet[r]:
                    # print("Hello0")
                    # print(num)
                    return False
                
                if num in colSet[c]:
                    # print("Hello1")
                    # print(num)
                    return False
                
                inner_row = r // 3
                inner_col = c // 3

                if num in boxSet[(inner_row, inner_col)]:
                    # print("Hello2")
                    # print(num)
                    return False
                
                rowSet[r].add(num)
                colSet[c].add(num)
                boxSet[(inner_row, inner_col)].add(num)

        
        return True