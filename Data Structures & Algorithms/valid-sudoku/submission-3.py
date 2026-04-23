class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        arr = [set() for i in range(10)]

        for c in range(9):
            for r in range(9):
                if board[r][c] != ".":
                    if board[r][c] in arr[c]:
                        return False
                    else:
                        arr[c].add(board[r][c])

        arr = [set() for i in range(10)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    if board[r][c] in arr[r]:
                        return False
                    else:
                        arr[r].add(board[r][c])

        
        arr = [set() for i in range(10)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                idx = (r//3) * 3 + (c//3)
                idx += 1

                if board[r][c] in arr[idx]:
                    return False
                else:
                    arr[idx].add(board[r][c])

        return True
        