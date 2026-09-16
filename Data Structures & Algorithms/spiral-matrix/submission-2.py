class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowLen, colLen = len(matrix), len(matrix[0])
        direction = 1
        row, col = 0, -1
        total = rowLen * colLen
        arr = []
        while len(arr) != total:
            for _ in range(colLen):
                col += direction
                arr.append(matrix[row][col])
            rowLen -= 1
            for _ in range(rowLen):
                row += direction
                arr.append(matrix[row][col])
            colLen -= 1
            direction *= -1

        return arr

