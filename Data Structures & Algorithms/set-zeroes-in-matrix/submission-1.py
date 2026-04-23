class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowLen, colLen = len(matrix), len(matrix[0])

        def changeMatrix(r,c):
            matrix[r][c] = "*"
            print(matrix)

            for i in range(0, r):
                if matrix[i][c] != 0:
                    matrix[i][c] = "*"
            

            for i in range(r, rowLen):
                if matrix[i][c] != 0:
                    matrix[i][c] = "*"

            for i in range(0, c):
                if matrix[r][i] != 0:
                    matrix[r][i] = "*"


            for i in range(c, colLen):
                if matrix[r][i] != 0:
                    matrix[r][i] = "*"

        for r in range(rowLen):
            for c in range(colLen):
                if matrix[r][c] == 0:
                    changeMatrix(r,c)
                    

        for r in range(rowLen):
            for c in range(colLen):
                if matrix[r][c] == "*":
                    matrix[r][c] = 0

 
