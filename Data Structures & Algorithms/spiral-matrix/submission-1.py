class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        direction = 1

        row, col = 0, -1

        res = []

        while rowLen > 0 and colLen > 0:
            for _ in range(colLen):
                col += direction
                res.append(matrix[row][col])

            rowLen -= 1
            for _ in range(rowLen):
                row += direction
                res.append(matrix[row][col])
            
            colLen -= 1

            direction *= -1

        return res